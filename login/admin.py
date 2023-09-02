from django.contrib import admin
from .models import CustomUser , Guide 
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'address', 'country_code', 'photo_url', 'languages','is_guide')

@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ('user_username', 'rate', 'is_approved', 'reviews', 'user_email', 'user_phone', 'user_address', 'user_country_code', 'user_photo_url', 'user_languages')

    def user_username(self, obj):
        return obj.user.username

    def user_email(self, obj):
        return obj.user.email

    def user_phone(self, obj):
        return obj.user.phone

    def user_address(self, obj):
        return obj.user.address

    def user_country_code(self, obj):
        return obj.user.country_code

    def user_photo_url(self, obj):
        return obj.user.photo_url

    def user_languages(self, obj):
        return obj.user.languages

    def user_session_message(self, obj):
        return obj.user.session_message

    user_username.short_description = 'Username'
    user_email.short_description = 'Email'
    user_phone.short_description = 'Phone'
    user_address.short_description = 'Address'
    user_country_code.short_description = 'Country Code'
    user_photo_url.short_description = 'Photo URL'
    user_languages.short_description = 'Languages'
    user_session_message.short_description = 'Session Message'    

