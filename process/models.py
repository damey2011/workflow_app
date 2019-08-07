from organization.models import *


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Process(BaseModel):
    user = models.ForeignKey(get_user_model(), related_name='createdprocesses', on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, related_name='processorg', on_delete=models.CASCADE)
    process_name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    isComplete = models.BooleanField(default=False)


class Stage(BaseModel):
    user = models.ForeignKey(get_user_model(), related_name='createdstage', on_delete=models.CASCADE)
    process = models.ForeignKey(Process, related_name='stages', on_delete=models.CASCADE)
    order = models.CharField(max_length=255)
    isComplete = models.BooleanField(default=False)


class Form(BaseModel):
    user = models.ForeignKey(get_user_model(), related_name='userforms', on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, related_name='orgforms', on_delete=models.CASCADE)
    form_name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    fields = models.TextField(max_length=255)


class Document(BaseModel):
    user = models.ForeignKey(get_user_model(), related_name='userdocuments', on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, related_name='orgdocuments', on_delete=models.CASCADE)
    filename = models.CharField(max_length=255,null=True)
    description = models.TextField(max_length=255,null=True)
    link = models.CharField(max_length=255)


class Tasks(BaseModel):
    user = models.ForeignKey(get_user_model(), related_name='createdtask', on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, related_name='tasks', on_delete=models.CASCADE)
    form = models.ForeignKey(Form, related_name='formtasks', on_delete=models.CASCADE, null=True)
    document = models.ForeignKey(Document, related_name='documenttasks', on_delete=models.CASCADE, null=True)
    users = models.ForeignKey(get_user_model(), related_name="tasks_to_user", on_delete=models.CASCADE, null=True)
    groups = models.ForeignKey(Groups, related_name="tasks_to_group", on_delete=models.CASCADE, null=True)
    isComplete = models.BooleanField(default=False)


class Formresponse(BaseModel):
    user = models.ForeignKey(get_user_model(), related_name='userformresponse', on_delete=models.CASCADE)
    form = models.ForeignKey(Form, related_name='formresponse', on_delete=models.CASCADE)
    response = models.TextField(max_length=255)
<<<<<<< HEAD
=======
    
>>>>>>> 4543e4b584c90a4da0fa2361af7000fe4312e199
