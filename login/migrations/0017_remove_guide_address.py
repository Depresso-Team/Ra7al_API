# Generated by Django 4.2.5 on 2023-09-14 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_alter_customuser_photo_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guide',
            name='address',
        ),
    ]