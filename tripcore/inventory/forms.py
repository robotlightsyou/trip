from django import forms
from .models import Fixture


class FixtureForm(forms.ModelForm):
    class Meta:
        model = Fixture
        fields = ['source']
