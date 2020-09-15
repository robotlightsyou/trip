from django.shortcuts import render

# Create your views here.


def rental_home(request):
    return render(request, 'rental/trip_rental.html', {'title': 'Rental - Home'})
