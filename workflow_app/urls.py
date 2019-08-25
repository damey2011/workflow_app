"""workflow_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Workflow801 API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('utility/', include('utils.urls', namespace='utils')),
    url(r'^schema/$', schema_view),
    url(r'^$', RedirectView.as_view(url='account/login', permanent=False)),  # login
    url(r'^account/', include('account.urls')),  # accounts app
    url(r'^org/', include('organization.urls')),
    url(r'^process/', include('process.urls')),

]
