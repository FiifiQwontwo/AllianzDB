from django.conf import settings
from django.db import models
from realtor.models import *
from furnishing.models import Furnishing
from .validators import validate_video_extension
import random
import string
from django.utils.text import slugify
from accounts.models import User
from build_material.models import Build


# Create your models here.
def randomise_slug():
    return ''.join(random.choice(string,ascii_letters + string.digits)for _ in range(5))

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=250)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    sqft = models.IntegerField(blank =True, null = True)
    lot_size = models.IntegerField(blank =True, null = True)
    garage = models.IntegerField(blank=True, null =True)
    pool = models.BooleanField(default=False)
    boys_quarters = models.BooleanField(default=False)
    self_compound = models.BooleanField(default=False)
    parking_space = models.BooleanField(default=False)
    brick_type = models.ForeignKey(Build, blank=True, null=True,on_delete=models.DO_NOTHING)
    build_condition = models.CharField(max_length=20, help_text='Newly Built or Renovated')
    furnished = models.ForeignKey(Furnishing,on_delete=models.DO_NOTHING)
    facilities = models.TextField(blank = True, help_text = 'Facilities in the apartment')
    date_listed = models.DateTimeField(default=datetime.now)
    agency_fee = models.BooleanField(default =True)
    main_image = models.ImageField(upload_to='main_image/&Y/&m/&d/')
    video_of = models.FileField(blank=True, upload_to='videos/&Y/&m/&d/',validators = [validate_video_extension],null=True, verbose_name="Video of Building")
    image_1 = models.ImageField(blank=True, upload_to='image_1/&Y/&m/&d/')
    image_2 = models.ImageField(blank=True, upload_to='image_2/&Y/&m/&d/')
    image_3 = models.ImageField(blank=True, upload_to='image_3/&Y/&m/&d/')
    image_4 = models.ImageField(blank=True, upload_to='image_4/&Y/&m/&d/')
    image_5 = models.ImageField(blank=True, upload_to='image_5/&Y/&m/&d/')
    image_6 = models.ImageField(blank=True, upload_to='image_6/&Y/&m/&d/')
    image_7 = models.ImageField(blank=True, upload_to='image_7/&Y/&m/&d/')
    image_8 = models.ImageField(blank=True, upload_to='image_8/&Y/&m/&d/')
    image_9 = models.ImageField(blank=True, upload_to='image_9/&Y/&m/&d/')
    image_10 = models.ImageField(blank=True, upload_to='image_10/&Y/&m/&d/')
    published = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, help_text='Enter any text', default='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title +'-' + randomise_slug())
        super(Listing, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
