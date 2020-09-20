from django.contrib import admin
# import inventory.models
from .models import Fixture, Source, Source_Type, Fixture_Type, Manufacturer

# Register your models here.
admin.site.register(Fixture)
admin.site.register(Fixture_Type)
admin.site.register(Source)
admin.site.register(Source_Type)
admin.site.register(Manufacturer)
