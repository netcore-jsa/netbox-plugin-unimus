from django.contrib import admin
from django import forms
from .model import UnimusIntegration
from django.core.exceptions import ValidationError
import requests


class UnimusForm(forms.ModelForm):
    class Meta:
        model = UnimusIntegration
        fields = '__all__'

    # This will be implemented when the python-unimus client is published.

    def clean_test(self):
        data = self.cleaned_data['Test']
        if not data:
            raise ValidationError("This is broken on purpose!")
        return data

    def clean_verify_certificate(self):
        data_verify_certificate = self.cleaned_data['Verify_Certificate']
        if data_verify_certificate:
            data_url = self.cleaned_data['Unimus_Address']
            try:
                requests.get(data_url)
            except requests.exceptions.SSLError:
                raise ValidationError("Not a valid SSL Cert")
        return data_verify_certificate


class UnimusAdmin(admin.ModelAdmin):
    change_form_template = 'admin/custom_change_form.html'
    form = UnimusForm
    list_display = ('Unimus_Address',
                    'API_Token',
                    'Verify_Certificate',
                    'Test_Unimus_Connection')


admin.site.register(UnimusIntegration, UnimusAdmin)
