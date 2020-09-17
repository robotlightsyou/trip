from django.db import models
from django.utils import timezone
# from django.cntrib.auth.models import User
from django.urls import reverse
from django.db import models
from django import forms

# RENT_STATUS_CHOICES = 

def choose_source(source):
    if source == 'led':
        return LED_KIND_CHOICES
    elif source == 'conventional':
        return CONVENTIONAL_KIND_CHOICES
    elif source == 'mover':
        return MOVER_KIND_CHOICES
    else:
        print('Invalid choice')
        # raise ValueError

SOURCE_CHOICES = (
    ('led', 'LED'),
    ('conventional', "Conventional"),
    ('mover', 'Mover')
)

LED_KIND_CHOICES = (
    ('rgb', 'RGB'),
    ('rgba', 'RGBA'),
    ('rgbw', 'RGBW'),
    ('rgbaw', 'RGBAW'),
    ('rgbawuv', 'RGBAWUV'),
    ('other', 'Other'),
)
CONVENTIONAL_KIND_CHOICES = (
    ('500', '500'),
    ('575', '575'),
    ('750', '750'),
    ('1_000', '1_000'),
)

MOVER_KIND_CHOICES = (
    ('led_mover', 'LED Mover'),
    ('lamp_mover', 'Lamped Mover'),
)

class Fixture(models.Model):
    #change to foreign key of users?
    owner = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)
    last_rented = models.DateTimeField(default=None)
    last_sickbay = models.DateTimeField(default=None)
    last_service = models.TextField()
    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES, default='conventional')
    # kind = models.CharField(max_length=20)
    # source = forms.CharField(max_length=15, label='Source:', widget = forms.Select(choices=SOURCE_CHOICES))
    # kind = forms.CharField(max_length=50, label='Source Kind', widget=forms.Select(choices=choose_source(source)), default='conventional')

# class LED(BASE):
#     source = models.CharField(max_length=20)
#     kind = models.CharField(max_length=20)

# class LED_Par(LED):
#     pass

# class LED_Strip(LED):
#     pass

# class LED_Leko(LED):
#     pass

# class Conventional(BASE):
#     source = models.CharField(max_length=20)
#     kind = models.CharField(max_length=20)

# class Parcan(Conventional):
#     pass

# class Leko(Conventional):
#     pass

# class Strip(Conventional):
#     pass

# class Fresnel(Conventional):
#     pass

# class Mover(BASE):
#    source = models.CharField(max_length=20)
#    kind = models.CharField(max_length=20)

# class LED_Mover(Mover):
#     pass

# class Lamp_Mover(Mover):
#     pass

class Projector(Fixture):
    pass

class Hardware(Fixture):
    pass
