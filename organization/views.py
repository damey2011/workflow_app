import cloudinary.uploader
from django.contrib.auth import get_user_model
from guardian.utils import get_anonymous_user
from rest_framework import filters
from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.mixins import UpdateModelMixin
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from organization.permissions import IsOwnerOrReadOnly
from organization.serializers import *


class OrganizationList(generics.ListCreateAPIView):
    '''A user can retrieve all organizations and create an organization
    Sample request: {"org_name":"department of Computer Science","description":"myDescription","logo":"Image Data"}'''
    serializer_class = OrganizationSerializer
    authentication_classes = (TokenAuthentication,)
    # parser_classes = (MultiPartParser, FormParser,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['org_name']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)  # permission for authenticated users and owner of Organization

    def get_queryset(self):
        queryset = Organization.objects.all()
        print(self.request.auth)
        user = self.request.user if self.request.user.is_authenticated else get_anonymous_user()  # handling unauthorized access
        return queryset

    def perform_create(self, serializer):
        user = self.request.user.id if self.request.user.is_authenticated else get_anonymous_user()  # handling unauthorized access
        image_file = self.request.data.get("logo")  # get the image from the data
        if image_file:
            result = cloudinary.uploader.upload(image_file, folder="workflow801")  # cloudinary upload
            image_public_id = result['public_id']  # store the public id cloudinary upload
            serializer.save(user_id=user, logo=image_public_id)  # save the public id in db
        else:
            serializer.save(user_id=user)


class UpdateOrg(UpdateModelMixin):
    def updateorg(self, request, *args, **kwargs):
        user = request.user.id if request.user.is_authenticated else get_anonymous_user()  # handling unauthorized access
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        return Response(self.perform_update(serializer))

    def perform_update(self, serializer):
        if serializer.is_valid():
            image = serializer.validated_data['logo']
            # if(image.size > 1000000):
            #     return get_api_response(ProfileStatusCodes.Profile_Pic_Size_Exceeded, httpStatusCode= status.HTTP_400_BAD_REQUEST)                            
            if image:
                result = cloudinary.uploader.upload(image, folder="workflow801")  # cloudinary upload
                image_public_id = result['public_id']  # store the public id cloudinary upload
                print(image_public_id)
                serializer.save(logo=image_public_id)  # save the public id in db
            else:
                serializer.save()
            return serializer.data


class OrganizationDetail(generics.RetrieveUpdateDestroyAPIView, UpdateOrg):
    '''Retrieve, modify or delete user created organization.'''
    queryset = Organization.objects.all()
    # parser_classes = (MultiPartParser, FormParser,)
    serializer_class = OrganizationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def put(self, request, *args, **kwargs):
        return self.updateorg(request, *args, **kwargs)


class UsertoOrgList(generics.ListCreateAPIView):
    '''A User can join an organization;
        Sample request: {"user_obj":"1", "org":"1"}'''
    serializer_class = UsertoOrgSerializer
    # parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)  # permission for authenticated users and owner of Organization

    def get_queryset(self):
        queryset = UsertoOrg.objects.all()
        user = self.request.user if self.request.user.is_authenticated else get_anonymous_user()  # handling unauthorized access
        return queryset

    def perform_create(self, serializer):
        admin = self.request.user.id if self.request.user.is_authenticated else get_anonymous_user()  # handling unauthorized access
        admin = get_user_model().objects.get(pk=admin)
        user_obj = self.request.data.get("user_obj")
        user_queryset = get_user_model().objects.get(pk=user_obj)
        org = self.request.data.get("org")
        org_queryset = Organization.objects.get(pk=org)
        serializer.save(admin=admin, user_obj=user_queryset, org=org_queryset)


class UsertoOrgDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Retrieve, modify or delete user created organization.'''
    queryset = UsertoOrg.objects.all()
    # parser_classes = (MultiPartParser, FormParser,)
    serializer_class = UsertoOrgSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class GroupsList(generics.ListCreateAPIView):
    '''A user can retrieve all Groupss and create an Groups
        Sample request: {"group_name":"Students","description":"myDescription","organization":"1"}'''
    serializer_class = GroupsSerializer
    # parser_classes = (MultiPartParser, FormParser,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['group_name']
    permission_classes = (
    permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)  # permission for authenticated users and owner of Groups

    def get_queryset(self):
        queryset = Groups.objects.all()
        user = self.request.user if self.request.user.is_authenticated else get_anonymous_user()  # handling unauthorized access
        return queryset

    def perform_create(self, serializer):
        user = self.request.user.id if self.request.user.is_authenticated else get_anonymous_user()  # handling unauthorized access
        serializer.save(user_id=user)


class GroupsDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Retreive, modify or delete group
        Useful when the user that created a group wants to modify it.
    '''
    queryset = Groups.objects.all()
    # parser_classes = (MultiPartParser, FormParser,)
    serializer_class = GroupsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class UsertoGroupsList(generics.ListCreateAPIView):
    '''A User can join an organization;
        Sample request: {"user_obj":"1","grp":"1,"org":"1"}'''
    serializer_class = UsertoGroupsSerializer
    # parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)  # permission for authenticated users and owner of Organization

    def get_queryset(self):
        queryset = UsertoGroups.objects.all()
        user = self.request.user if self.request.user.is_authenticated else get_anonymous_user()  # handling unauthorized access
        return queryset

    def perform_create(self, serializer):
        admin = self.request.user.id if self.request.user.is_authenticated else get_anonymous_user()  # handling unauthorized access
        admin = get_user_model().objects.get(pk=admin)
        user_obj = self.request.data.get("user_obj")
        user_queryset = get_user_model().objects.get(pk=user_obj)
        org = self.request.data.get("org")
        grp = self.request.data.get("grp")
        org_queryset = Organization.objects.get(pk=org)
        grp_queryset = Groups.objects.get(pk=grp)
        serializer.save(admin=admin, user_obj=user_queryset, org=org_queryset, grp=grp_queryset)


class UsertoGroupsDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Retreive, modify or delete user to group
    '''
    queryset = UsertoGroups.objects.all()
    # parser_classes = (MultiPartParser, FormParser,)
    serializer_class = UsertoGroupsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
