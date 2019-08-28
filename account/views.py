import cloudinary.uploader
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views.decorators.csrf import requires_csrf_token
from rest_framework import filters
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.mixins import UpdateModelMixin
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from organization.permissions import IsAdminOrReadOnly

from organization.models import *
from .authentication import *
from .serializers import *
from process.views import send_email

@requires_csrf_token
@api_view(['POST'])
def login_user(request, format=None):
    '''Sample request: {"email":"ogbanugot@gmail.com","password":"mypass"}
    '''
    if request.user.is_authenticated:
        return Response(status=status.HTTP_200_OK)

    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            user_serializer = ProfileSerializer(user)
            token, _ = Token.objects.get_or_create(user=user.id)
            is_expired, token = token_expire_handler(token)
            obj = Organization.objects.get(pk=1)
            if IsAdminOrReadOnly.has_object_permission(user, obj) == True:
                isAdmin = True
            else:
                isAdmin = False
            try:                
                privilege_group = Groups.objects.get(hasPrivilege = True)
                user_in_privilege_group = UsertoGroups.objects.filter(user_obj=user, grp=privilege_group.id)
                if user_in_privilege_group is not None:
                    hasPrivilege = True
                else:
                    hasPrivilege = False
            except:
                hasPrivilege = False
            login(request, user)
            return Response({"Token": token.key, "Expires_in": expires_in(token),"isAdmin":isAdmin,"hasPrivilege": hasPrivilege, "User": user_serializer.data},
                            status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def logout_user(request):
    logout(request)
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def sign_up(request, format=None):
    '''Sample request: {"email":"ogbanugot@gmail.com","password":"mypass","first_name":"ogban","last_name":"ugot", "phone_number":"08092343839"}
    '''
    if request.user.is_authenticated:
        return Response(status=status.HTTP_200_OK)

    serializer = SignUpSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data["email"]
        first_name = serializer.validated_data["first_name"]
        last_name = serializer.validated_data["last_name"]
        phone_number = serializer.validated_data["phone_number"]
        user = get_user_model().objects.create_user(email=email, username=email,
                                                    password=serializer.validated_data["password"],
                                                    first_name=first_name,
                                                    last_name=last_name,
                                                    phone_number=phone_number)
        user_serializer = ProfileSerializer(user)
        token = Token.objects.get(user=user.id)
        subject = "Welcome to workflow801!"
        html = """\
                    <html>
                    <body>
                    <p>Hi there</p>
                    <p>Thanks for signing up on the demo build for the "workflow801" workflow management system.</p> 
                    <p>Be sure to help us test the web application by trying out all the features available.</p>
                    <p>You can also send us feedback at workflow801@gmail.com</p>
                    <p>Warm regards,</p>
                    <p>Dev team.</p>
                    </body>
                    </html>
                    """
        send_email(email,subject, html)
        return Response({"Token": token.key, "Expires_in": expires_in(token),"isAdmin":False,"hasPrivilege": False, "User": user_serializer.data}, status=201)
    return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class UserList(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    # parser_classes = (MultiPartParser, FormParser,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'email']

    def get_queryset(self):
        queryset = get_user_model().objects.all()
        return queryset

    def perform_create(self, serializer):
        image_file = self.request.data.get("profile_pic")  # get the image from the data
        if image_file:
            result = cloudinary.uploader.upload(image_file, folder="workflow801")  # cloudinary upload
            image_public_id = result['public_id']  # store the public id cloudinary upload
            serializer.save(profile_pic=image_public_id)  # save the public id in db
        else:
            serializer.save()


class UpdateProfile(UpdateModelMixin):

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(id=self.request.user.id)
        self.check_object_permissions(self.request, obj)
        return obj

    def updateprofile(self, request, *args, **kwargs):
        user = request.user.id if request.user.is_authenticated else get_anonymous_user()  # handling unauthorized access
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        return Response(self.perform_update(serializer))

    def perform_update(self, serializer):
        if serializer.is_valid():
            image = serializer.validated_data['profile_pic']
            # if(image.size > 1000000):
            #     return get_api_response(ProfileStatusCodes.Profile_Pic_Size_Exceeded, httpStatusCode= status.HTTP_400_BAD_REQUEST)                            
            if image:
                result = cloudinary.uploader.upload(image, folder="workflow801")  # cloudinary upload
                image_public_id = result['public_id']  # store the public id cloudinary upload
                print(image_public_id)
                serializer.save(profile_pic=image_public_id)  # save the public id in db
            else:
                serializer.save()
            return serializer.data


class UserDetail(generics.RetrieveUpdateDestroyAPIView, UpdateProfile):
    '''Retrieve, modify or delete user.'''
    queryset = get_user_model().objects.all()
    # parser_classes = (MultiPartParser, FormParser,)
    serializer_class = ProfileSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(id=self.request.user.id)
        self.check_object_permissions(self.request, obj)
        return obj

    def put(self, request, *args, **kwargs):
        return self.updateprofile(request, *args, **kwargs)

