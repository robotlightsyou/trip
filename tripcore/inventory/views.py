from django.shortcuts import render

# Create your views here.


def inventory_home(request):
    return render(request, 'inventory/inventory_base.html', {'title': 'Inventory - Home'})


def company(request):
    return render(request, 'inventory/company.html', {'title': 'Inventory - Company'})


def out(request):
    return render(request, 'inventory/out.html', {'title': 'Inventory - Rented Out'})


def personal(request):
    return render(request, 'inventory/personal.html', {'title': 'Inventory - Owned'})
