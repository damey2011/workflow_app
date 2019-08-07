from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework import serializers

from process.models import Form


class FormBuilderSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        models = Form
        fields = (
            'id',
            'user',
            'content',
            'description',
            'organization'
        )
