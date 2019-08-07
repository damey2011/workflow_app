from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework import serializers

from process.formbuilder.utils import get_readable_form_data
from process.models import Form, Formresponse


class FormBuilderSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = (
            'id',
            'user',
            'content',
            'description',
            'organization'
        )


class FormResponseSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Formresponse
        fields = '__all__'

    def to_representation(self, instance):
        data = super(FormResponseSerializer, self).to_representation(instance)
        data['response'] = get_readable_form_data(data.get('fb_data'))
        del data['fb_data']
        return data
