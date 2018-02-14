from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Person, Beer, Store, Order, Trip
from .forms import PersonForm, BeerForm, StoreForm, TripForm, OrderForm

def index(request):
    return HttpResponse("Hello, world. You're at Myapps index.")

def ApiPersonGetView(request, pk=None):
	person = Person.objects.get(pk=pk)
	name = person.name
	age = person.age
	return JsonResponse({'name':name, 'age':age})

def ApiBeerGetView(request, pk=None):
	beer = Beer.objects.get(pk=pk)
	beer_type = beer.beer_type
	size = beer.size
	name = beer.name
	price = beer.price
	bottle_type = beer.bottle_type
	return JsonResponse({'name':name,'beer_type':beer_type, 'size':size, 'price':price, 'bottle_type':bottle_type})

def ApiCreatePerson(request):
	if request.method == 'POST':
		form = PersonForm(request.POST)
		if form.is_valid():
			person = Person()
			person.name = form.cleaned_data['name']
			person.age = form.cleaned_data['age']
			person.save()

			return redirect(person)
	else:
		form = PersonForm()

	return render(request, 'myapp/person_form.html', {'form': form})

