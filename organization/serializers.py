from rest_framework.serializers import HyperlinkedModelSerializer
from organization.models import *
from django.contrib.auth.models import User
from rest_framework import serializers
from django.conf import settings
from account.models import User
from rest_framework.validators import UniqueValidator

#Add feilds for users
class OrganizationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.id")
    org_name = models.CharField(max_length=255, 
    validators=[UniqueValidator(queryset=get_user_model().objects.all(), message="An organization with that name already exists.")])
    # groups = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = Organization
        fields = ('id',
                'user',
                'org_name',
                'description',
                'logo',
                # 'groups',
                # 'usertoorgs',
                # 'usertoorgtogroups',
                # 'processorg',
                # 'orgforms',
                # 'orgdocuments')
        )
    def create(self, validated_data):
        return Organization.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.org_name = validated_data.get('org_name',instance.org_name)
        instance.description = validated_data.get('description',instance.description)
        instance.logo = validated_data.get('logo',instance.logo)
        return instance
    

class GroupsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Groups
        fields = ('id','organization', 'group_name','description','usertogroups','tasks_to_group')
        
    def create(self, validated_data):
        return Groups.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.group_name = validated_data.get('group_name',instance.group_name)
        instance.description = validated_data.get('description',instance.description)
        instance.organization = validated_data.get('organization',instance.organization)
        return instance
        
class UsertoOrgSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsertoOrg
        fields = ('id','user_obj','org')
        
    # def create(self, validated_data):
    #     return UsertoOrg.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.org = validated_data.get('org',instance.org)
    #     return instance

class UsertoGroupsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UsertoGroups
        fields = ('id','user_obj','org','grp')
        
    # def create(self, validated_data):
    #     return UsertoGroups.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.org = validated_data.get('org',instance.org)
    #     instance.grp = validated_data.get('grp',instance.group)
    #     return instance