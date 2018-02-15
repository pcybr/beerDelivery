from django import forms
from .models import Beer, Store, Order, Person, Trip

class PersonForm(forms.Form):
	name = forms.CharField(max_length = 90)
	age = forms.IntegerField(min_value = 0)

class BeerForm(forms.Form):
	TOPS = (
		('Twist-Off', 'Twist-Off'),
		('Pop-Off', 'Pop-Off'),
		('Can', 'Can'),
	)
	TYPES = (
        ('IPA', 'IPA'),
        ('Light', 'Light'),
        ('Lager', 'Lager'),
        ('Ale', 'Ale'),
        ('Non-Alcoholic', 'Non-Alcoholic')
    )
	size = forms.IntegerField(min_value = 0)
	name = forms.CharField(max_length = 100)
	price = forms.IntegerField(min_value = 0)
	beer_type = forms.ChoiceField(choices = TYPES, widget = forms.Select())
	bottle_type = forms.ChoiceField(choices = TOPS, widget = forms.Select())

class StoreForm(forms.Form):
	inventory = forms.ModelMultipleChoiceField(queryset = Beer.objects.all())
	#inventory = forms.CharField(max_length = 100)
	location = forms.CharField(max_length = 100)
	name = forms.CharField(max_length = 100);

class OrderForm(forms.Form):
	buyer = forms.ModelChoiceField(queryset = Person.objects.all())
	item = forms.ModelChoiceField(queryset = Beer.objects.all())

class TripForm(forms.Form):
	store = forms.ModelChoiceField(queryset = Store.objects.all())
	runner = forms.ModelChoiceField(queryset = Person.objects.all())



