# Generated by Django 4.2.4 on 2023-09-14 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_alter_guide_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='license',
            field=models.IntegerField(default=0),
        ),
    ]
