from django.contrib import admin

# Register your models here.
from .models import Organization, Groups, UsertoOrg, UsertoGroups

admin.site.register(Organization)
admin.site.register(Groups)
admin.site.register(UsertoOrg)
admin.site.register(UsertoGroups)
