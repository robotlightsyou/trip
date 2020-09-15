from django.shortcuts import render

# Create your views here.


def checkout(request):
    return render(request, 'rental/checkout.html', {'title': 'Rental - Check Out'})


def checkin(request):
    return render(request, 'rental/checkin.html', {'title': 'Rental - Check In'})
