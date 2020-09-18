from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Fixture

# Create your views here.


def inventory_home(request):
    return render(request, 'inventory/inventory_base.html', {'title': 'Inventory - Home'})


def company(request):
    return render(request, 'inventory/company.html', {'title': 'Inventory - Company'})


def out(request):
    return render(request, 'inventory/out.html', {'title': 'Inventory - Rented Out'})


def personal(request):
    return render(request, 'inventory/personal.html', {'title': 'Inventory - Owned'})

# add changes per simpleisbetter... method
class FixtureListView(ListView):
    model = Fixture
    context_object_name = 'fixtures'

class FixtureCreateView(CreateView):
    model = Fixture
    fields = ('owner', 'date_added', 'last_rented', 'last_sickbay', 'last_service',
              'model', 'manufacturer', 'source', 'kind')
    success_url = reverse_lazy('fixture_list')

class FixtureUpdateView(UpdateView):
    model = Fixture
    fields = ('owner', 'date_added', 'last_rented', 'last_sickbay', 'last_service',
              'model', 'manufacturer', 'source', 'kind')
    success_url = reverse_lazy('fixture_list')
