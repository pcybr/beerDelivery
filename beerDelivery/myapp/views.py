from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Person, Beer, Store, Order, Trip

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