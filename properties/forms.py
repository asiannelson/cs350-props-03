from django import forms
from django.forms import Form

class LookupForm(Form):
	search = forms.CharField(widget=forms.TextInput, label="Search Properties")
	
class DistanceForm(Form):
	address = forms.CharField(widget=forms.TextInput, label="Address")
	distance = forms.IntegerField(widget=forms.NumberInput, label="Distance")