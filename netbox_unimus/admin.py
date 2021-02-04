from django.contrib import admin
from django import forms
from .model import UnimusIntegration
from django.core.exceptions import ValidationError


class UnimusForm(forms.ModelForm):
    class Meta:
        model = UnimusIntegration
        fields = '__all__'

    def clean_Test(self):
        data = self.cleaned_data['Test']
        if not data:
            raise ValidationError("This is broken on purpose!")
        return data


class UnimusAdmin(admin.ModelAdmin):
    form = UnimusForm
    list_display = ('Unimus_Address',
                    'API_Token',
                    'Verify_Certificate',
                    'Test')


admin.site.register(UnimusIntegration, UnimusAdmin)
