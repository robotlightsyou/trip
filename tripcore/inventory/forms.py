from django import forms
from .models import Fixture, Fixture_Type, Source, Source_Type, Manufacturer


class FixtureForm(forms.ModelForm):
    class Meta:
        model = Fixture
        fields = ['owner', 'date_added', 'last_rented', 'last_sickbay',
                  'last_service', 'manufacturer', 'fixture_type',
                  'source', 'source_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['source_type'].queryset = Source_Type.objects.none()
        self.fields['fixture_type'].queryset = Fixture_Type.objects.none()

        if 'manufacturer' in self.data:
            try:
                manufacturer_id = int(self.data.get('manufacturer'))
                self.fields['fixture_type'].queryset = Fixture_Type.objects.filter(manufacturer_id=manufacturer_id).order_by('name')
            except (TypeError, ValueError):
                pass
        elif self.instance.pk:
            self.fields['fixture_type'].queryset = self.instance.manufacturer.fixture_type_set.order_by('name')

        if 'source' in self.data:
            try:
                source_id = int(self.data.get('source'))
                self.fields['source_type'].queryset = Source_Type.objects.filter(source_id=source_id).order_by('name')
            except (TypeError, ValueError):
                pass
        elif self.instance.pk:
            self.fields['source_type'].queryset = self.instance.source.source_type_set.order_by('name')
