from django.urls import path
from inventory import views as iviews

urlpatterns = [
    path('', iviews.inventory_home, name='trip_inventory-home'),
    path('company/', iviews.company, name='trip_inventory-company'),
    path('out/', iviews.out, name='trip_inventory-out'),
    path('personal/', iviews.personal, name='trip_inventory-personal'),
]
