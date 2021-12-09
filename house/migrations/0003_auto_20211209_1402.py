# Generated by Django 2.1.7 on 2021-12-09 14:02

from django.db import migrations, models
import house.validators


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0002_auto_20211208_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='video_of',
            field=models.FileField(null=True, upload_to='videos/&Y/&m/&d/', validators=[house.validators.validate_video_extension], verbose_name=''),
        ),
    ]
