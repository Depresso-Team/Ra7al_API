# Generated by Django 4.2.4 on 2023-09-14 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_guide_tours'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='guided_tours',
        ),
        migrations.RemoveField(
            model_name='guide',
            name='tours',
        ),
    ]
