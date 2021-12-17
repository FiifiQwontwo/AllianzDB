from datetime import datetime
from django.conf import settings
from django.db import models


# Create your models here.

class Build(models.Model):
    build_type = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)
