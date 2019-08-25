from rest_framework import serializers

from process.models import *


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'user_id', 'organization', 'filename', 'description', 'link', 'documenttasks')


class FormresponseSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source="user_id.email", read_only=True)
    form = serializers.CharField(source="form.form_name", read_only=True)

    class Meta:
        model = Formresponse
        fields = ('id', 'user_id', 'form', 'response')

    def to_representation(self, instance):
        data = super(FormresponseSerializer, self).to_representation(instance)


class FormSerializer(serializers.ModelSerializer):
    formresponse = FormresponseSerializer(many=True, read_only=True)

    class Meta:
        model = Form
        fields = ('id', 'user_id', 'config', 'user', 'organization', 'form_name', 'description', 'formtasks',
                  'formresponse')


class TaskSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source="user.id")

    class Meta:
        model = Tasks
        fields = ('id', 'user_id', 'stage', 'document', 'form', 'groups', 'users', 'isComplete')


class StageSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Stage
        fields = ('id', 'name', 'user_id', 'process', 'order', 'isComplete', 'tasks')


class ProcessSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source="user.id")
    stages = StageSerializer(many=True, read_only=True)

    class Meta:
        model = Process
        fields = ('id', 'user_id', 'organization', 'process_name', 'description', 'isComplete', 'stages')
