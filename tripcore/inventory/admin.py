from django.contrib import admin
# import inventory.models
from .models import Fixture, Source, Kind

# Register your models here.
admin.site.register(Fixture)
admin.site.register(Source)
admin.site.register(Kind)
