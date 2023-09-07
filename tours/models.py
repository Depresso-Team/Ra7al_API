from django.db import models

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


class ToursList(models.Model):
    name = models.CharField(max_length=100)
    state_id = models.CharField(max_length=2, choices=STATES)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    status = models.BooleanField(default=True) 
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
