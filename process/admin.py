from django.contrib import admin

# Register your models here.
from .models import Process, Stage, Tasks, Document, Form, Formresponse

admin.site.register(Process)
admin.site.register(Stage)
admin.site.register(Tasks)
admin.site.register(Document)
admin.site.register(Form)
admin.site.register(Formresponse)
