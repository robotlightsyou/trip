from django.urls import path
from landing import views as lviews

urlpatterns = [
    path('', lviews.landing_home, name='trip_landing-home'),
]
