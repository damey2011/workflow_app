from django.db import models
from django.utils import timezone
from django.conf import settings  
from django.contrib.auth import get_user_model
from organization.models import *

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Process(BaseModel):
    user = models.ForeignKey(get_user_model(), related_name='createdprocesses', on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, related_name='processorg', on_delete=models.CASCADE)
    process_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=255)
    
class Stage(BaseModel):
    user = models.ForeignKey(get_user_model(), related_name='createdstage', on_delete=models.CASCADE)
    process = models.ForeignKey(Process, related_name='stages', on_delete=models.CASCADE)
    order = models.CharField(max_length=255)
    groups = models.ForeignKey(Groups, related_name="stages_to_group", on_delete=models.CASCADE,null=True)
    users = models.ForeignKey(get_user_model(), related_name="stages_to_user", on_delete=models.CASCADE, null=True)

class Form(BaseModel):
    user = models.ForeignKey(get_user_model(),related_name='userforms',on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization,related_name='orgforms', on_delete=models.CASCADE)
    form_name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    fields = models.TextField(max_length=255)

class Document(BaseModel):
    user = models.ForeignKey(get_user_model(),related_name='userdocuments',on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, related_name='orgdocuments', on_delete=models.CASCADE)
    file = models.FileField(max_length=255) #Filefield?

class Tasks(BaseModel):
    user = models.ForeignKey(get_user_model(), related_name='createdtask', on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage,related_name='tasks', on_delete=models.CASCADE)
    form = models.ForeignKey(Form, related_name='formtasks', on_delete=models.CASCADE, null=True)
    document = models.ForeignKey(Document, related_name='documenttasks', on_delete=models.CASCADE, null=True)

class Formresponse(BaseModel):
    user = models.ForeignKey(get_user_model(),related_name='userformresponse',on_delete=models.CASCADE)
    form = models.ForeignKey(Form,related_name='formresponse', on_delete=models.CASCADE)
    response = models.TextField(max_length=255)
    