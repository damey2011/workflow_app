from django.conf import settings
from django.urls import path

from utils import views

app_name = 'utilities'

urlpatterns = [

]

if settings.DEBUG:
    urlpatterns += [
        path('db-export/', views.ExportDatabaseView.as_view(), name='export-db')
    ]
