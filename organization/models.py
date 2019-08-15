from django.contrib.auth import get_user_model
from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Organization(BaseModel):
    user = models.ForeignKey(get_user_model(), related_name='createdorgs', on_delete=models.CASCADE)
    org_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=255)
    logo = models.ImageField(null=True, blank=False)


class Groups(BaseModel):
    user = models.ForeignKey(get_user_model(), related_name='createdgroups', on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, related_name='groups', on_delete=models.CASCADE)
    group_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=255)


class UsertoOrg(BaseModel):
    admin = models.ForeignKey(get_user_model(), related_name='add_user_organizations', on_delete=models.CASCADE)
    user_obj = models.ForeignKey(get_user_model(), related_name='userorganizations', on_delete=models.CASCADE)
    org = models.ForeignKey(Organization, related_name='usertoorgs', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user_obj', 'org']


class UsertoGroups(BaseModel):
    admin = models.ForeignKey(get_user_model(), related_name='add_user_groups', on_delete=models.CASCADE)
    user_obj = models.ForeignKey(get_user_model(), related_name='usergroups', on_delete=models.CASCADE)
    org = models.ForeignKey(Organization, related_name='usertoorgtogroups', on_delete=models.CASCADE)
    grp = models.ForeignKey(Groups, related_name='usertogroups', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user_obj', 'org', 'grp']
