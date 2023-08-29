# Import the necessary module from Django
from django.contrib import admin
# Import your User and Guide models from application
from .models import User, Guide

# Register your models with the admin site
admin.site.register(User)
admin.site.register(Guide)
