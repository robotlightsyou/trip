from django.urls import path
from users import views as uviews

urlpatterns = [
    path('', uviews.users_home, name='trip_users-home'),
]
