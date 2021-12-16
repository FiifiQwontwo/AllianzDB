from django.db import models
from datetime import datetime
from django.utils.text import slugify
import string
import random


def randy_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(9))


# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    firm_name = models.CharField(max_length=100, default='Vida Properties')
    photo = models.ImageField(upload_to='realtor/%Y/%m/%d/')
    email = models.CharField(max_length=100, unique=True)
    phone = models.CharField(unique=True, max_length=20)
    description = models.TextField(blank=True)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    slug = models.SlugField(unique=True, help_text='Enter any text', default='')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + "-" + randy_slug())
        super(Realtor, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
