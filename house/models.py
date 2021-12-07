from django.db import models
from realtor.models import *
from furnishing.models import Furnishing
import random
import string
from django.utils.text import slugify


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
    sqft = models.IntegerField()
    lot_size = models.IntegerField()
    garage = models.IntegerField(blank=True, null =True)
    pool = models.BooleanField(default=False)
    boys_quarters = models.BooleanField(default=False)
    self_compound = models.BooleanField(default=False)
    build_condition = models.CharField(max_length=20, help_text='Newly Built or Renovated')
    furnished = models.ForeignKey(Furnishing,on_delete=models.DO_NOTHING)
    facilities = models.TextField(blank = True, help_text = 'Facilities in the apartment')
    date_listed = models.DateTimeField(default=datetime.now)
    agency_fee = models.BooleanField(default =True)
    main_image = models.ImageField(upload_to='main_image/&Y/&m/&d/')
    image_1 = models.ImageField(blank=True, upload_to='image1/&Y/&m/&d/')
    image_2 = models.ImageField(blank=True, upload_to='image2/&Y/&m/&d/')
    image_3 = models.ImageField(blank=True, upload_to='image3/&Y/&m/&d/')
    image_4 = models.ImageField(blank=True, upload_to='image4/&Y/&m/&d/')
    image_5 = models.ImageField(blank=True, upload_to='image5/&Y/&m/&d/')
    image_6 = models.ImageField(blank=True, upload_to='image6/&Y/&m/&d/')
    published = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, help_text='Enter any text', default='')

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title +'-' + randomise_slug())
            super(Realtor, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
