# Generated by Django 4.2.4 on 2023-09-14 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_guide_address_guide_age_guide_license'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='Identity',
            field=models.TextField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
