from django.core.validators import RegexValidator
from django.db import models
from extras.models import ChangeLoggedModel

class UnimusIntegration(ChangeLoggedModel):
    Unimus_Address = models.URLField()
    API_Token = models.TextField(validators=[RegexValidator(regex='^.{101}$', message='Length has to be 101', code='nomatch')])
    Verify_Certificate = models.BooleanField(default=False)
    Test = models.BooleanField(default=True)

    def clean_task_for(self):
        data = self.clean_task_for('task_for')
