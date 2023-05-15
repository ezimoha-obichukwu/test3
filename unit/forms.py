from django import forms

class PollingUnitResultForm(forms.Form):
    party = forms.CharField(max_length=100)
    result = forms.IntegerField()
