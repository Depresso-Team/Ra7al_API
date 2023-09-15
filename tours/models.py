from django.db import models
from login.models import Guide


STATES = [
    ('1', 'Cairo'),
    ('2', 'Alexandria'),
    ('3', 'Giza'),
    ('4', 'Luxor'),
    ('5', 'Aswan'),
    ('6', 'Asyut'),
    ('7', 'Beheira'),
    ('8', 'Beni Suef'),
    ('9', 'Dakahlia'),
    ('10', 'Damietta'),
    ('11', 'Faiyum'),
    ('12', 'Gharbia'),
    ('13', 'Ismailia'),
    ('14', 'Kafr El Sheikh'),
    ('15', 'Matrouh'),
    ('16', 'Minya'),
    ('17', 'Monufia'),
    ('18', 'New Valley'),
    ('19', 'North Sinai'),
    ('20', 'Port Said'),
    ('21', 'Qalyubia'),
    ('22', 'Qena'),
    ('23', 'Red Sea'),
    ('24', 'Sharqia'),
    ('25', 'Sohag'),
    ('26', 'South Sinai'),
    ('27', 'Suez'),
    ('28', '6th of October'),
    ('29', 'Helwan'),
    ('30', '15th of May'),
    ('31', '10th of Ramadan'),
]

class Reviews (models.Model):
    tour = models.ForeignKey('ToursList',on_delete=models.CASCADE)
    review = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.tour)
    

def default_tour_photo():
    return 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjDnVewOoTokof2aeNRf_3H7k2kfnYIa5Tjg&usqp=CAU'

class ToursList(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.PositiveIntegerField(default=0)
    state_id = models.CharField(max_length=2, choices=STATES)
    company_name = models.CharField(max_length=100)
    duration = models.IntegerField()
    location = models.CharField(max_length=100)
    status = models.BooleanField(default=True) 
    message = models.TextField(blank=True, null=True)
    rate = models.FloatField(default=0.0)
    saved = models.BooleanField(default=False)
    guide = models.ForeignKey(Guide, on_delete=models.SET_NULL, null=True, blank=True)
    photo = models.ImageField(upload_to='tours',null=True, blank=True ,default=default_tour_photo)


    def __str__(self):
        return self.name



