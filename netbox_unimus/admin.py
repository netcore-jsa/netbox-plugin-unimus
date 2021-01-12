from django.contrib import admin
from .model import UnimusIntegration


@admin.register(UnimusIntegration)
class BgpPeeringAdmin(admin.ModelAdmin):
    list_display = ('Unimus_Address',
                    'API_Token',
                    'Verify_Certificate',
                    'Test')