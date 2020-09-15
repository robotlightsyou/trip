from django.urls import path
from rental import views as rviews

urlpatterns = [
    path('checkin', rviews.checkin, name='trip_checkin'),
    path('checkout', rviews.checkout, name='trip_checkout'),
]
