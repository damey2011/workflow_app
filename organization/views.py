from organization.models import *
from rest_framework.views import APIView
from organization.serializers import *
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from django.core import serializers
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from organization.permissions import IsOwnerOrReadOnly
from rest_framework.parsers import FormParser, MultiPartParser
from django.contrib.auth import get_user_model
from guardian.utils import get_anonymous_user
import cloudinary.uploader
from rest_framework import viewsets
from rest_framework import filters
#

class OrganizationList(generics.ListCreateAPIView):
    '''A user can retrieve all organizations and create an organization
    Sample request: {"org_name":"department of Computer Science","Description":"myDescription","logo":"Image Data"}'''
    serializer_class = OrganizationSerializer
    parser_classes = (MultiPartParser, FormParser,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['org_name']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)#permission for authenticated users and owner of Organization

    def get_queryset(self):
        queryset = Organization.objects.all()
        user = self.request.user if self.request.user.is_authenticated else get_anonymous_user() #handling unauthorized access
        return queryset

    def perform_create(self, serializer):
        user = self.request.user.id if self.request.user.is_authenticated else get_anonymous_user() #handling unauthorized access
        image_file = self.request.data.get("logo") #get the image from the data
        if image_file:
            result = cloudinary.uploader.upload(image_file, folder = "workflow801") #cloudinary upload
            image_public_id = result['public_id']  #store the public id cloudinary upload
            serializer.save(user_id=user, logo = image_public_id) #save the public id in db
        else:
            serializer.save(user_id=user) 

class OrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Retrieve, modify or delete user created organization.'''
    queryset = Organization.objects.all()
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = OrganizationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)               


class UsertoOrgList(generics.ListCreateAPIView):
    '''A User can join an organization;
        Sample request: {"org":"1"}'''
    serializer_class = UsertoOrgSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)#permission for authenticated users and owner of Organization

    def get_queryset(self):
        queryset = UsertoOrg.objects.all()
        user = self.request.user if self.request.user.is_authenticated else get_anonymous_user() #handling unauthorized access
        return queryset

    def perform_create(self, serializer):
        user = self.request.user.id if self.request.user.is_authenticated else get_anonymous_user() #handling unauthorized access
        org = self.request.data.get("org")
        org_queryset = Organization.objects.get(pk=org)
        serializer.save(user_id=user, org=org_queryset) 

class UsertoOrgDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Retrieve, modify or delete user created organization.'''
    queryset = UsertoOrg.objects.all()
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = UsertoOrgSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)     


class GroupsList(generics.ListCreateAPIView):
    '''A user can retrieve all Groupss and create an Groups
        Sample request: {"group_name":"Students","description":"myDescription","organization":"1"}'''
    serializer_class = GroupsSerializer
    parser_classes = (MultiPartParser, FormParser,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['group_name']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)#permission for authenticated users and owner of Groups

    def get_queryset(self):
        queryset = Groups.objects.all()
        user = self.request.user if self.request.user.is_authenticated else get_anonymous_user() #handling unauthorized access
        return queryset

    def perform_create(self, serializer):
        user = self.request.user.id if self.request.user.is_authenticated else get_anonymous_user() #handling unauthorized access       
        serializer.save(user_id=user) 

class GroupsDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Retreive, modify or delete group
        Useful when the user that created a group wants to modify it.
    '''
    queryset = Groups.objects.all()
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = GroupsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)               



class UsertoGroupsList(generics.ListCreateAPIView):
    '''A User can join an organization;
        Sample request: {"grp":"1,"org":"1"}'''
    serializer_class = UsertoGroupsSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)#permission for authenticated users and owner of Organization

    def get_queryset(self):
        queryset = UsertoGroups.objects.all()
        user = self.request.user if self.request.user.is_authenticated else get_anonymous_user() #handling unauthorized access
        return queryset

    def perform_create(self, serializer):
        user = self.request.user.id if self.request.user.is_authenticated else get_anonymous_user() #handling unauthorized access
        org = self.request.data.get("org")
        grp = self.request.data.get("grp")
        org_queryset = Organization.objects.get(pk=org)
        grp_queryset = Groups.objects.get(pk=grp)
        serializer.save(user_id=user,org=org_queryset,grp=grp_queryset) 

class UsertoGroupsDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Retreive, modify or delete user to group
    '''
    queryset = UsertoGroups.objects.all()
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = UsertoGroupsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)               


# # @api_view(["GET", "DELETE"])
# # def removeUserFromGroup(request, pk):
# #     '''Delete a particular group for a particular user (In an organization).
# #         Used when a user wants to delete themselves from a group in an organization.
# #     '''
# #     ids = fks.split(",")
# #     try:
# #         group = UsertoGroups.objects.filter(user_id=ids[0], grp_id=ids[1])
# #     except group.DoesNotExist:
# #         return Response(status=status.HTTP_404_NOT_FOUND)

# #     if request.method == 'DELETE':
# #         serializer = UsertoGroupsSerializer(group)
# #         if serializer.validated_data["user"] != self.request.user:
# #             raise exceptions.PermissionDenied(detail='You do not have permission.')
# #         group.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)

# class removeUserFromGroup(generics.RetrieveDestroyAPIView):
#     '''Delete a particular group for a particular user (In an organization).
#         Used when a user wants to delete themselves from a group in an organization.
#     '''
#     queryset = UsertoGroups.objects.all()
#     parser_classes = (MultiPartParser, FormParser,)
#     serializer_class = UsertoGroupsSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)#permission for authenticated users and owner of Organization

#     def get_object(self):
#         queryset = self.filter_queryset(self.get_queryset())
#         # make sure to catch 404's below
#         obj = queryset.filter(user_id=self.request.user)
#         self.check_object_permissions(self.request, obj)
#         return obj

#     def perform_destroy(self,instance):
#         org = self.kwargs['org']
#         grp = self.kwargs['grp']
#         org_queryset = Organization.objects.get(pk=org)
#         grp_queryset = Groups.objects.get(pk=grp)
#         group = instance.objects.filter(org=org_queryset,grp=grp_queryset)
#         group.delete()