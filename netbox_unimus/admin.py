from django.contrib import admin
from django import forms
from .model import UnimusIntegration
from django.core.exceptions import ValidationError
import requests


class UnimusForm(forms.ModelForm):
    class Meta:
        model = UnimusIntegration
        fields = '__all__'

    # This will be implimented when the python-unimus client is published.

    def clean_Test(self):
        data = self.cleaned_data['Test']
        if not data:
            raise ValidationError("This is broken on purpose!")
        return data


    def clean_Verify_Certificate(self):

        data_Verify_Certificate = self.cleaned_data['Verify_Certificate']
        if data_Verify_Certificate:
            data_url = self.cleaned_data['Unimus_Address']
            try:
                requests.get(data_url)
            except requests.exceptions.SSLError:
                raise ValidationError("Not a valid SSL Cert")
        return data_Verify_Certificate

class UnimusAdmin(admin.ModelAdmin):
    form = UnimusForm
    list_display = ('Unimus_Address',
                    'API_Token',
                    'Verify_Certificate',
                    'Test')


admin.site.register(UnimusIntegration, UnimusAdmin)
