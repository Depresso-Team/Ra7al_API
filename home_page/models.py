from django.db import models

# Create your models here.

# Slider Model For Home Page 
class SliderPhoto(models.Model):
    title = models.CharField(max_length=200)
    photo_url = models.ImageField(upload_to='photos/', null=True, blank=True)

    def __str__(self):
        return self.title
    

class Bannar(models.Model):
    title = models.CharField(max_length=50)
    bannar_url = models.ImageField(upload_to='banners/', null=True, blank=True)

    def __str__(self):
        return self.title