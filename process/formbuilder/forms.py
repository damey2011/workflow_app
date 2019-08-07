from django import forms

from process.models import Form


class CreateFormForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = (
            'user',
            'organization',
            'config',
            'form_name'
        )
        widgets = {
            'user': forms.HiddenInput,
            'organization': forms.HiddenInput,
            'config': forms.HiddenInput
        }
