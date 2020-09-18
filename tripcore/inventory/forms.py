from django import forms
from .models import Fixture


class FixtureForm(forms.ModelForm):
    class Meta:
        model = Fixture
        fields = ['source']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kind'].queryset = Kind.objects.none()
