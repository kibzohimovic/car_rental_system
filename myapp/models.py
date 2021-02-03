from django.db import models

#### Create your models here.

#creating our turples for choices for the drop down
LOCATION_CHOICES = (
    ('MK', 'MUKONO'),
    ('KA', 'KAMPALA'),
    ('KI', 'KIREKA'),
    ('GZ', 'GAYAZA'),
    ('SA', 'SEETA'),
    ('BE','BWEYOGERERE'),
    ('BA','BANDA'),
    ('KE','KAWEMPE'),
    ('MA','MAKINDYE')
)

CAR_CHOICES = (
    ('BW','BMW'),
    ('AI','AUDI'),
    ('LS','Lexus')
)

ENGINE_TYPE_CHOICES = (
    ('DL','DIESEL'),
    ('PO','PETROL')
)

TRANSMISSION_CHOICES = (
    ('AO','AUTOMATIC'),
    ('ML','MANUAL')
)

#model for a user booking a car on the first page
class BookCarModel(models.Model):
    location = models.CharField(max_length=100, choices = LOCATION_CHOICES, default = 'KA')
    pick_date = models.DateField(auto_now=False, auto_now_add=False)
    return_date = models.DateField(auto_now=False, auto_now_add=False)
    choose_car = models.CharField(max_length=100, choices = CAR_CHOICES, default = 'BW')


#model for displaying available cars on the cars page
class DisplayCarsModel(models.Model):
    car_name = models.CharField(max_length=100, choices= CAR_CHOICES, default = 'BW')
    car_image = models.ImageField(upload_to = 'images/') #folder where images will be uploaded to
    ac_availability = models.BooleanField(default = True)
    description = models.TextField(max_length = 1000, default = 'Great Car')
    engine_type = models.CharField(max_length = 100, choices = ENGINE_TYPE_CHOICES, default = 'PO')
    transmission = models.CharField(max_length=100, choices = TRANSMISSION_CHOICES, default = 'AO')
    price = models.IntegerField(default = 120000)