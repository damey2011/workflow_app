from django.conf.urls import url
from django.urls import include

from . import views

urlpatterns = [
    url(r'^$', views.ProcessList.as_view()),  # list all Process
    url(r'^(?P<pk>[0-9]+)/$', views.ProcessDetail.as_view()),  # get a particular Process

    url(r'^stage/$', views.StageList.as_view()),  # List Stage
    url(r'^stage/(?P<pk>[0-9]+)/$', views.StageDetail.as_view(), ),  # Particular stage

    url(r'^stage/task$', views.TaskList.as_view()),  # List Task
    url(r'^stage/task/(?P<pk>[0-9]+)/$', views.TaskDetail.as_view(), ),  # Particular Task

    url(r'^form/$', views.FormList.as_view()),  # list Form
    url(r'^form/(?P<pk>[0-9]+)/$', views.FormDetail.as_view()),  # get a particular Form

    url(r'^document/$', views.DocumentList.as_view()),  # List Document
    url(r'^document/(?P<pk>[0-9]+)/$', views.DocumentDetail.as_view(), ),  # get a particular document

    url(r'^formbuilder/', include('process.formbuilder.urls')),

    url(r'^form/formresponse/$', views.FormresponseList.as_view()),  # List Formresponse
    url(r'^form/formresponse/(?P<org>[0-9]+)/$', views.FormresponseDetail.as_view(), ),  # get a particular Formresponse

    url(r'^processflow/$', views.processflow, )  # Process flow
]
