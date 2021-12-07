# Generated by Django 2.1.7 on 2021-12-05 21:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('furnishing', '0001_initial'),
        ('realtor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('sqft', models.IntegerField()),
                ('lot_size', models.IntegerField()),
                ('garage', models.IntegerField(blank=True)),
                ('pool', models.BooleanField(default=False)),
                ('boys_quarters', models.BooleanField(default=False)),
                ('self_compound', models.BooleanField(default=False)),
                ('build_condition', models.CharField(help_text='Newly Built or Renovated', max_length=20)),
                ('facilities', models.TextField(blank=True, help_text='Facilities in the apartment')),
                ('date_listed', models.DateTimeField(default=datetime.datetime.now)),
                ('agency_fee', models.BooleanField(default=True)),
                ('main_image', models.ImageField(upload_to='main_image/&Y/&m/&d/')),
                ('image_1', models.ImageField(blank=True, upload_to='image1/&Y/&m/&d/')),
                ('image_2', models.ImageField(blank=True, upload_to='image2/&Y/&m/&d/')),
                ('image_3', models.ImageField(blank=True, upload_to='image3/&Y/&m/&d/')),
                ('image_4', models.ImageField(blank=True, upload_to='image4/&Y/&m/&d/')),
                ('image_5', models.ImageField(blank=True, upload_to='image5/&Y/&m/&d/')),
                ('image_6', models.ImageField(blank=True, upload_to='image6/&Y/&m/&d/')),
                ('published', models.BooleanField(default=False)),
                ('furnished', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='furnishing.Furnishing')),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtor.Realtor')),
            ],
        ),
    ]