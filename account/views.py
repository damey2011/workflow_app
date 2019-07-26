from .serializers import *
import cloudinary.uploader
from rest_framework import filters
from rest_framework import status
from django.utils import timezone
from django.db import IntegrityError
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.mixins import UpdateModelMixin
from django.http import HttpResponse, JsonResponse
from account.permissions import IsOwnerOrReadOnly
from rest_framework.parsers import FormParser, MultiPartParser
from .profileResponseHelper import get_api_response, ProfileStatusCodes
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from django.contrib.auth import authenticate,login, logout, get_user_model


@requires_csrf_token
@api_view(['POST'])
def login_user(request, format=None):
    '''Sample request: {"email":"ogbanugot@gmail.com","password":"mypass"}
    '''
    if request.user.is_authenticated:
        return Response(status = status.HTTP_200_OK)

    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)        

@api_view(['GET'])
def logout_user(request):
    logout(request)
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def sign_up(request, format=None):
    '''Sample request: {"email":"ogbanugot@gmail.com","password":"mypass","first_name":"ogban","last_name":"ugot", "phone_number":"08092343839"}
    '''
    if request.user.is_authenticated:
        return Response(status = status.HTTP_200_OK)

    serializer = SignUpSerializer(data=request.data)
    if serializer.is_valid():
            email = serializer.validated_data["email"]
            first_name = serializer.validated_data["first_name"]
            last_name = serializer.validated_data["last_name"]           
            user = get_user_model().objects.create_user(email=email, username=email, 
                                                password = serializer.validated_data["password"],
                                                first_name=first_name,
                                                last_name=last_name)
            return Response(serializer.data, status=201)                     
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    parser_classes = (MultiPartParser, FormParser,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name','last_name','email']

    def get_queryset(self):
        queryset = get_user_model().objects.all()
        return queryset

    def perform_create(self, serializer):
        image_file = self.request.data.get("profile_pic") #get the image from the data
        if image_file:
            result = cloudinary.uploader.upload(image_file, folder = "workflow801") #cloudinary upload
            image_public_id = result['public_id']  #store the public id cloudinary upload
            serializer.save(profile_pic = image_public_id) #save the public id in db
        else:
            serializer.save() 


class UpdateProfile(UpdateModelMixin):

    def get_object(self):        
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(id=self.request.user.id)
        self.check_object_permissions(self.request, obj)
        return obj
        
    def updateprofile(self, request, *args, **kwargs):
        user = request.user.id if request.user.is_authenticated else get_anonymous_user() #handling unauthorized access
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)   
        return Response(self.perform_update(serializer,user))

    def perform_update(self, serializer, user):
        if serializer.is_valid():
            image = serializer.validated_data['profile_pic']
            # if(image.size > 1000000):
            #     return get_api_response(ProfileStatusCodes.Profile_Pic_Size_Exceeded, httpStatusCode= status.HTTP_400_BAD_REQUEST)                            
            if image:
                result = cloudinary.uploader.upload(image, folder = "workflow801") #cloudinary upload
                image_public_id = result['public_id']  #store the public id cloudinary upload
                print(image_public_id)
                serializer.save(user_id=user, profile_pic=image_public_id) #save the public id in db
            else:
                serializer.save(user_id=user) 
            return serializer.data 

class UserDetail(generics.RetrieveUpdateDestroyAPIView, UpdateProfile):
    '''Retrieve, modify or delete user.'''
    queryset = get_user_model().objects.all()
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = ProfileSerializer

    def get_object(self):        
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(id=self.request.user.id)
        self.check_object_permissions(self.request, obj)
        return obj
    
    def put(self, request, *args, **kwargs):
        return self.updateprofile(request, *args, **kwargs)     
 
        

