from django.contrib import admin
from .models import CustomUser, Guide


# Register the CustomUser model with the admin site.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'address', 'country_code', 'photo_url', 'languages', 'is_guide')

# Register the Guide model with the admin site.
@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ('user_username', 'rate', 'is_approved', 'reviews', 'user_email', 'user_phone', 'user_address', 'user_country_code', 'user_photo_url', 'user_languages')

    # Define custom methods to access user-related fields from the Guide model.
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

    # Customize the column headers in the admin interface.
    user_username.short_description = 'Username'
    user_email.short_description = 'Email'
    user_phone.short_description = 'Phone'
    user_address.short_description = 'Address'
    user_country_code.short_description = 'Country Code'
    user_photo_url.short_description = 'Photo URL'
    user_languages.short_description = 'Languages'
