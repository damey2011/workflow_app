from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model


from organization.models import *
from process.serializers import *
from account.serializers import *

class UsertoOrgSerializer(serializers.ModelSerializer):
    user_obj = serializers.SlugField(max_length=50, min_length=None, allow_blank=False)
    org = serializers.CharField(source="org.org_name", read_only=True)
    class Meta:
        model = UsertoOrg
        fields = ('id', 'user_obj', 'org')


class UsertoGroupsSerializer(serializers.ModelSerializer):
    user_obj = serializers.SlugField(max_length=50, min_length=None, allow_blank=False)
    org = serializers.CharField(source="org.org_name", read_only=True)
    grp = serializers.CharField(source="grp.group_name", read_only=True)
    class Meta:
        model = UsertoGroups
        fields = ('id', 'user_obj', 'org', 'grp')

class GroupsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    usertogroups = UsertoGroupsSerializer(many=True, read_only=True)

    class Meta:
        model = Groups
        fields = ('id', 'organization', 'group_name', 'description','usertogroups')

class OrganizationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.id")
    org_name = models.CharField(max_length=255,
                                validators=[UniqueValidator(queryset=get_user_model().objects.all(),
                                                            message="An organization with that name already exists.")])
    groups = GroupsSerializer(many=True, read_only=True)
    usertoorgs = UsertoOrgSerializer(many=True, read_only=True)
    usertoorgtogroups = UsertoGroupsSerializer(many=True, read_only=True)
    processorg = ProcessSerializer(many=True, read_only=True)
    orgforms = FormSerializer(many=True, read_only=True)
    orgdocuments = DocumentSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = ('id',
                  'user',
                  'org_name',
                  'description',
                  'logo',
                  'groups',
                  'usertoorgs',
                  'usertoorgtogroups',
                  'processorg',
                  'orgforms',
                  'orgdocuments')
                
