from django.conf import settings
from django.db import models
from accounts.models import User


# Create your models here.

class Furnishing(models.Model):
    furnished_name = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.furnished_name
