# Generated by Django 4.2.4 on 2023-09-15 16:58

from django.db import migrations, models
import login.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0018_guide_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo_url',
            field=models.ImageField(blank=True, default=login.models.default_photo_url, null=True, upload_to='users/'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='personal_photo',
            field=models.ImageField(blank=True, default=login.models.default_personal_photo, null=True, upload_to='guides/'),
        ),
    ]
