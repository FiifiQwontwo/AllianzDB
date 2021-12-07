from django.db import models


# Create your models here.

class Furnishing(models.Model):
    furnished_name = models.CharField(max_length=20)

    def __str__(self):
        return self.furnished_name
