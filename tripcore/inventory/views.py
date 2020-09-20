from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Fixture, Fixture_Type, Source_Type, Manufacturer, Source
from .forms import FixtureForm

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
    form_class = FixtureForm
    # fields = ('owner', 'date_added', 'last_rented', 'last_sickbay', 'last_service',
    #           'model', 'manufacturer', 'source', 'kind')
    success_url = reverse_lazy('fixture_list')


class FixtureUpdateView(UpdateView):
    model = Fixture
    form_class = FixtureForm
    # fields = ('owner', 'date_added', 'last_rented', 'last_sickbay', 'last_service',
    #           'model', 'manufacturer', 'source', 'kind')
    success_url = reverse_lazy('fixture_list')


def load_source_types(request):
    source_id = request.GET.get('source')
    source_types = Source_Type.objects.filter(
        source_id=source_id).order_by('name')
    return render(request, 'inventory/source_type_dropdown_options.html', {'source_types': source_types})


def load_fixture_types(request):
    manufacturer_id = request.GET.get('manufacturer')
    fixture_types = Fixture_Type.objects.filter(
        manufacturer_id=manufacturer_id).order_by('name')
    return render(request, 'inventory/fixture_type_dropdown_options.html', {'fixture_types': fixture_types})
