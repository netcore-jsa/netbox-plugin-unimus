from django.core.validators import RegexValidator
from django.db import models


class UnimusIntegration(models.Model):
    Unimus_Address = models.URLField()
    API_Token = models.TextField(validators=[RegexValidator(regex='^.{101}$', message='Length has to be 101', code='nomatch')])
    Verify_Certificate = models.BooleanField(default=False)
    Test_Unimus_Connection = models.BooleanField(default=True)
