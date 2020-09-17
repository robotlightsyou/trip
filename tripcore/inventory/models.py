from django.db import models
from django.utils import timezone
# from django.cntrib.auth.models import User
from django.urls import reverse
from django.db import models

class LED(models.Model):
    pass

class LED_Par(LED):
    pass

class LED_Strip(LED):
    pass

class LED_Leko(LED):
    pass

class Conventional(models.Model):
    pass

class Parcan(Conventional):
    pass

class Leko(Conventional):
    pass

class Strip(Conventional):
    pass

class Fresnel(Conventional):
    pass

class Mover(models.Model):
    pass

class LED_Mover(Mover):
    pass

class Lamp_Mover(Mover):
    pass

class Projector(models.Model):
    pass

class Hardware(models.Model):
    pass
