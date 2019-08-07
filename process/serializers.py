from rest_framework import serializers

from process.models import *


class ProcessSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source="user.id")

    class Meta:
        model = Process
        fields = ('id', 'user_id', 'organization', 'process_name', 'description', 'isComplete', 'stages')


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ('id', 'user_id', 'process', 'order', 'isComplete', 'tasks')


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id','user_id','organization','filename','description','link','documenttasks')


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ('id', 'user_id', 'organization', 'form_name', 'description', 'fields', 'formtasks', 'formresponse')


class TaskSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source="user.id")

    class Meta:
        model = Tasks
        fields = ('id', 'user_id', 'stage', 'document', 'form', 'groups', 'users', 'isComplete')


class FormresponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formresponse
        fields = ('id', 'user_id', 'form', 'response')
