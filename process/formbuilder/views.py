import json
from copy import copy

from django.forms import model_to_dict
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from process.formbuilder.forms import CreateFormForm
from process.models import Form, Formresponse, FormResponseFile
from process.serializers import FormSerializer


class CreateFormView(APIView):
    permission_classes = (IsAuthenticated,)
    template_name = 'forms/create-form.html'
    form_class = CreateFormForm

    def get(self, request, *args, **kwargs):
        ctx = {
            'form': self.form_class(initial={
                'organization': self.kwargs.get('organization_id'),
                'user': self.request.user.id
            }),
            'submit_url': self.request.build_absolute_uri()
        }
        return render_to_response(self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        serializer = FormSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UpdateFormView(APIView):
    template_name = 'forms/create-form.html'
    form_class = CreateFormForm

    def get_object(self):
        return get_object_or_404(Form, pk=self.kwargs.get('form_id'))

    def get(self, request, *args, **kwargs):
        ctx = {
            'form': self.form_class(initial={
                'organization': self.kwargs.get('organization_id'),
                'user': self.request.user.id,
                **model_to_dict(self.get_object())
            }),
            'is_update': True,
            'submit_url': self.request.build_absolute_uri()
        }
        return render_to_response(self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        serializer = FormSerializer(instance=self.get_object(), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class ViewForm(APIView):
    template_name = 'forms/view-form.html'

    def get_object(self):
        return get_object_or_404(Form, pk=self.kwargs.get('form_id'))

    def get_user_form_responses(self, one=False):
        frs = Formresponse.objects.filter(form=self.get_object(), user=self.request.user)
        if one:
            return frs.first()
        return frs

    def get(self, request, *args, **kwargs):
        ctx = {
            'form_config': json.dumps(self.get_object().config),
            'submit_url': self.request.build_absolute_uri()
        }
        if self.get_user_form_responses().exists():
            ctx['form_config'] = self.get_user_form_responses(True).fb_data
        return render_to_response(self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        data = request.POST
        files = request.FILES
        form_data = copy(data)
        fb_data = form_data.pop('fb_data', {})
        if self.get_user_form_responses().exists():
            form_response = self.get_user_form_responses(True)
        else:
            form_response = Formresponse.objects.create(user=request.user, form=self.get_object(), response=form_data,
                                                        fb_data=json.loads(fb_data[0]))
        for key, file in files.items():
            frf = FormResponseFile.objects.create(form_response=form_response, file=file, field_name=key)
            form_data[key] = frf.file.url
        form_response.response = form_data
        form_response.save()
        return Response(form_data, status=status.HTTP_200_OK)


class TestFormView(TemplateView):
    template_name = 'forms/test-form.html'
