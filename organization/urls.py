from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.OrganizationList.as_view()),  # list all Organizations
    url(r'^(?P<pk>[0-9]+)/$', views.OrganizationDetail.as_view()),  # get a particular Organization
    url(r'^joinorg/$', views.UsertoOrgList.as_view()),  # Add user to organization
    url(r'^removeuserfromorg/(?P<pk>[0-9]+)/$', views.UsertoOrgDetail.as_view(), ),
    # remove a user from an organizations

    url(r'^groups/$', views.GroupsList.as_view()),  # list all Groups
    url(r'^groups/(?P<pk>[0-9]+)/$', views.GroupsDetail.as_view()),  # get a particular Group
    url(r'^joingroup/$', views.UsertoGroupsList.as_view()),  # Add user to group
    url(r'^removeuserfromgroup/(?P<org>[0-9]+)/$', views.UsertoGroupsDetail.as_view(), ),
    # get or delete a particular group belonging to a User in a particular organization

]
