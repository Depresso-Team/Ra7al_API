# Generated by Django 4.2.4 on 2023-09-13 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_guide_saved'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuidesReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=500)),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.guide')),
            ],
        ),
    ]
