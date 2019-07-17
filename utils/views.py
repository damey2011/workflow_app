from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render

from django.views import View

from utils.utility import generate_db_dump


class ExportDatabaseView(View):
    def get(self, request, *args, **kwargs):
        file = generate_db_dump()
        response = HttpResponse(content=file.read(), content_type='application/*')
        response['Content-Disposition'] = 'inline; filename={}'.format(file.name)
        return response
