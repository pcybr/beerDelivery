from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Person, Beer, Store, Order, Trip
from django.views.generic.edit import DeleteView

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

def ApiStoreGetView(request, pk=None):
	store = Store.objects.get(pk=pk)
	inv = store.inventory
	location = store.location
	name = store.name
	return JsonResponse({'name':name,'inventory':inv, 'location':location})


def ApiTripGetView(request, pk=None):
	trip = Trip.objects.get(pk=pk)
	runner = trip.runner.name
	buyers = trip.buyers.name
	store = trip.store
	time_created = trip.time_created
	active = trip.active
	orders = trip.orders
	return JsonResponse({'runner':runner,'buyers':buyers, 'store':store, 'time':time_created, 'active':active, 'orders':orders})



def ApiOrderGetView(request, pk=None):
	order = Order.objects.get(pk=pk)
	buyer = order.buyer
	item = order.item
	return JsonResponse({'order':order,'buyer':buyer, 'item':item})

def ApiPersonDeleteView(request, pk=None):
	person = Person.objects.get(pk=pk)
    person.delete()
    return HttpResponse("Deleted!")
