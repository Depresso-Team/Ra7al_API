# Generated by Django 4.2.4 on 2023-09-14 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0002_bannar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannar',
            name='bannar_url',
            field=models.ImageField(upload_to='banners'),
        ),
        migrations.AlterField(
            model_name='sliderphoto',
            name='photo_url',
            field=models.ImageField(upload_to='photos'),
        ),
    ]
