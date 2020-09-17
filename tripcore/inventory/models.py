from django.db import models
from django.utils import timezone
# from django.cntrib.auth.models import User
from django.urls import reverse
from django.db import models
from django import forms

# RENT_STATUS_CHOICES = 

class Fixture(models.Model):
    #change to foreign key of users?
    owner = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)
    last_rented = models.DateTimeField(default=None)
    last_sickbay = models.DateTimeField(default=None)
    last_service = models.TextField()
    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    source = models.CharField(max_length=20)
    kind = models.CharField(max_length=20)

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
