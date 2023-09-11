from django.db import models

# Create your models here.

# Slider Model For Home Page 
class SliderPhoto(models.Model):
    title = models.CharField(max_length=200)
    photo_url = models.URLField()

    def __str__(self):
        return self.title