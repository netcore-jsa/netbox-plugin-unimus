from extras.plugins import PluginTemplateExtension
from django.db import models

class UnimusStatus(PluginTemplateExtension):
    model = 'dcim.device'

    def right_page(self):
        return self.render('inc/device_extension.html')
        async def status():
            return False


template_extensions = [UnimusStatus]
