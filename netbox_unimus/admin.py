from django.contrib import admin
from django import forms
from .model import UnimusIntegration


class UnimusForm(forms.ModelForm):
    class Meta:
        model = UnimusIntegration
        fields = '__all__'

class UnimusAdmin(admin.ModelAdmin):
    form = UnimusForm
    list_display = ('Unimus_Address',
                    'API_Token',
                    'Verify_Certificate',
                    'Test')

admin.site.register(UnimusIntegration, UnimusAdmin)