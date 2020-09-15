from django.shortcuts import render

# Create your views here.


def landing_home(request):
    return render(request, 'landing/trip_landing.html', {'title': 'TRIP - Home'})
