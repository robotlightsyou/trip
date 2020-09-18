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

SELECT_SOURCE = ('select_source', 'Select Source')


def get_kind(parent_type):
    if parent_type == 'led':
        # return LED_KIND_CHOICES
        return models.CharField(max_length=20, choices=LED_KIND_CHOICES, default='select_source')
    elif parent_type == 'conventional':
        # return CONVENTIONAL_KIND_CHOICES
        return models.CharField(max_length=20, choices=CONVENTIONAL_KIND_CHOICES, default='select_source')
    elif parent_type == 'mover':
        # return MOVER_KIND_CHOICES
        return models.CharField(max_length=20, choices=MOVER_KIND_CHOICES, default='select_source')
    else:
        print('Invalid choice')
        # raise ValueError

# add classes per https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html


class Source(models.Model):
    name = models.CharField(
        max_length=20, choices=SOURCE_CHOICES, default='conventional')

    def __str__(self):
        return self.name


class Kind(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=20, choices=SOURCE_CHOICES, default='conventional')


class Fixture(models.Model):
    # change to foreign key of users?
    owner = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)
    last_rented = models.DateTimeField(default=None)
    last_sickbay = models.DateTimeField(default=None)
    last_service = models.TextField()
    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    source = models.ForeignKey(Source, on_delete=models.SET_NULL, null=True)
    kind = models.ForeignKey(Kind, on_delete=models.SET_NULL, null=True)
    # source = models.CharField(max_length=20, choices=SOURCE_CHOICES, default='conventional')
    # kind = get_kind(source)
    # kind = models.CharField(max_length=20, choices=choose_source(source) or SELECT_SOURCE, default = 'select_source')
    # source = forms.CharField(max_length=15, label='Source:', widget = forms.Select(choices=SOURCE_CHOICES))
    # kind = forms.CharField(max_length=50, label='Source Kind', widget=forms.Select(choices=choose_source(source)), default='conventional')

    def __str__(self):
        return ' '.join([self.manufacturer, self.model])

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk':self.pk})


# class LED(BASE):
#     source = models.CharField(max_length=20)
#     kind = models.CharField(max_length=20)

# class LED_Par(LED):
#     pass

# class LED_Strip(LED):
#     pass

# class LED_Leko(LED):
#     pas

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
