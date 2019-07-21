from rest_framework.serializers import HyperlinkedModelSerializer
from process.models import *
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.conf import settings
from rest_framework.validators import UniqueValidator

#Add feilds for users
class ProcessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Process
        fields = ('id','user_id','organization','process_name','description','stages')

class StageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stage
        fields = ('id','user_id','process', 'order','groups','users','tasks')


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ('id','user_id','organization','file','documenttasks')
        
class FormSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Form
        fields = ('id','user_id','organization','form_name','description','fields','formtasks','formresponse')

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tasks
        fields = ('id','user_id','stage','document','form')

class FormresponseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Formresponse
        fields = ('id','user_id','form','response')