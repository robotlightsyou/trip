from django import forms

class FixtureForm(forms.ModelForm):
    class Meta:
        model = Fixture
        fields = ['source']
