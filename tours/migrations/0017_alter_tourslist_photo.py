# Generated by Django 4.2.4 on 2023-09-14 20:50

from django.db import migrations, models
import tours.models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0016_tourslist_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourslist',
            name='photo',
            field=models.ImageField(default=tours.models.default_tour_photo, upload_to='tours'),
        ),
    ]
