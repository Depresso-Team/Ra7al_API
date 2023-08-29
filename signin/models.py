from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.sessions.models import Session

LANGUAGES = [
    ("en", "English"),
    ("es", "Spanish"),
    ("fr", "French"),
    ("de", "German"),
    ("it", "Italian"),
    ("pt", "Portuguese"),
    ("nl", "Dutch"),
    ("ru", "Russian"),
    ("ja", "Japanese"),
    ("zh-cn", "Chinese (Simplified)"),
    ("ar", "Arabic"),
    ("hi", "Hindi"),
    ("ko", "Korean"),
    ("tr", "Turkish"),
    ("pl", "Polish"),
    ("uk", "Ukrainian"),
    ("cs", "Czech"),
    ("sv", "Swedish"),
    ("ro", "Romanian"),
    ("hu", "Hungarian"),
    ("vi", "Vietnamese"),
    ("el", "Greek"),
    ("th", "Thai"),
    ("he", "Hebrew"),
    ("id", "Indonesian"),
    ("da", "Danish"),
    ("fi", "Finnish"),
    ("no", "Norwegian"),
    ("bn", "Bengali"),
    ("ta", "Tamil"),
    ("hr", "Croatian"),
    ("fa", "Persian"),
    ("sk", "Slovak"),
    ("sl", "Slovenian"),
    ("ms", "Malay"),
    ("et", "Estonian"),
    ("lt", "Lithuanian"),
    ("lv", "Latvian"),
    ("sr", "Serbian"),
    ("sw", "Swahili"),
    ("tl", "Tagalog"),
    ("is", "Icelandic"),
    ("ka", "Georgian"),
    ("hy", "Armenian"),
    ("ur", "Urdu"),
    ("uz", "Uzbek"),
    ("kk", "Kazakh"),
    ("az", "Azerbaijani"),
    ("ky", "Kyrgyz"),
    ("bn", "Bengali"),
    ("gu", "Gujarati"),
    ("mr", "Marathi"),
    ("ne", "Nepali"),
    ("pa", "Punjabi"),
    ("si", "Sinhala"),
    ("ta", "Tamil"),
    ("te", "Telugu"),
    ("ml", "Malayalam"),
    ("kn", "Kannada"),
    ("or", "Odia"),
    ("as", "Assamese"),
    ("my", "Burmese"),
    ("dz", "Dzongkha"),
    ("km", "Khmer"),
    ("lo", "Lao"),
    ("mn", "Mongolian"),
    ("my", "Burmese"),
    ("ne", "Nepali"),
    ("ps", "Pashto"),
    ("sd", "Sindhi"),
    ("tg", "Tajik"),
    ("tk", "Turkmen"),
    ("ug", "Uighur"),
    ("ur", "Urdu"),
    ("yi", "Yiddish"),
]

class User(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.PositiveIntegerField(unique=True)
    email_address = models.EmailField(unique=True)
    address = models.CharField(max_length=200)
    country_code = models.PositiveIntegerField()
    languages = models.CharField(max_length=50, choices=LANGUAGES)
    photo_url = models.URLField()
    session_message = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return self.name



class Guide(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.PositiveIntegerField(unique=True)
    email_address = models.EmailField(unique=True)
    address = models.CharField(max_length=200)
    country_code = models.PositiveIntegerField()
    languages = models.CharField(max_length=50, choices=LANGUAGES)
    photo_url = models.URLField()
    rate = models.FloatField(default=0.0)
    reviews = models.TextField(max_length=255)    
    session_message = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name



@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        message = f"New user '{instance.name}' has been created! Welcome aboard!"
        instance.session_message = message
        instance.save()



@receiver(post_save, sender=Guide)
def guide_created(sender, instance, created, **kwargs):
    if created:
        message = f"New guide '{instance.name}' has been created! Welcome aboard!"
        instance.session_message = message
        instance.save()