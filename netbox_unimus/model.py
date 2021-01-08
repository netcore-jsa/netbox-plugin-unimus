from django.core.validators import RegexValidator
from django.db import models
from extras.models import ChangeLoggedModel

class UnimusIntegration(ChangeLoggedModel):
    Unimus_Address = models.URLField()
    API_Token = models.TextField(validators=[RegexValidator(regex='^.{101}$', message='Length has to be 101', code='nomatch')])
    Use_SSL = models.BooleanField(default = False)