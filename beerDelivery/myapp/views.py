from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Person, Beer, Store, Order, Trip
from django.views.generic.edit import DeleteView
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

def ApiStoreGetView(request, pk=None):
	store = Store.objects.get(pk=pk)
	inv = store.inventory
	location = store.location
	name = store.name
	return JsonResponse({'name':name,'inventory':inv, 'location':location})

def ApiTripGetView(request, pk=None):
	trip = Trip.objects.get(pk=pk)
	runner = trip.runner.name
	store = trip.store.name
	time_created = trip.time_created
	active = trip.active
	#orders = trip.orders
	return JsonResponse({'runner':runner, 'store':store, 'time':time_created, 'active':active})

def ApiOrderGetView(request, pk=None):
	order = Order.objects.get(pk=pk)
	buyer = order.buyer.name
	item = order.item.name
	return JsonResponse({'order':order.order_id,'buyer':buyer, 'item':item})

def ApiPersonDeleteView(request, pk=None):
	person = Person.objects.get(pk=pk)
	person.delete()
	return HttpResponse("Deleted!")

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

def ApiCreateBeer(request):
	if request.method == 'POST':
		form = BeerForm(request.POST)
		if form.is_valid():
			beer = Beer()
			beer.size = form.cleaned_data['size']
			beer.name = form.cleaned_data['name']
			beer.price = form.cleaned_data['price']
			beer.beer_type = form.cleaned_data['beer_type']
			beer.bottle_type = form.cleaned_data['bottle_type']
			beer.save()

			return redirect(beer)
	else:
		form = BeerForm()

	return render(request, 'myapp/beer_form.html', {'form': form})

def ApiCreateStore(request):
	if request.method == 'POST':
		form = StoreForm(request.POST)
		if form.is_valid():
			store = Store()
			store.inventory = form.cleaned_data['inventory']
			store.name = form.cleaned_data['name']
			store.location = form.cleaned_data['location']
			store.save()

			return redirect(store)
	else:
		form = StoreForm()

	return render(request, 'myapp/store_form.html', {'form': form})

def ApiCreateOrder(request):
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			order = Order()
			order.buyer = form.cleaned_data['buyer']
			#order.buyer = request.user
			order.item = form.cleaned_data['item']
			order.save()

			return redirect(order)
	else:
		form = OrderForm()

	return render(request, 'myapp/order_form.html', {'form': form})

def ApiCreateTrip(request):
	if request.method == 'POST':
		form = TripForm(request.POST)
		if form.is_valid():
			trip = Trip()
			#trip.runner = request.user
			trip.runner = form.cleaned_data['runner']
			trip.store = form.cleaned_data['store']
			trip.active = True
			trip.save()

			return redirect(trip)
	else:
		form = TripForm()

	return render(request, 'myapp/trip_form.html', {'form': form})

def ApiUpdatePerson(request, pk):
	person = Person.objects.get(pk=pk)
	if request.method == 'POST':
		form = PersonForm(request.POST)
		if form.is_valid():
			person.name = form.cleaned_data['name']
			person.age = form.cleaned_data['age']
			person.save()

			return redirect(person)
	else:
		form = PersonForm(initial={'name': person.name, 'age': person.age})

	return render(request, 'myapp/person_update.html', {'form': form, 'person_name': person.name})

def ApiUpdateBeer(request, pk):
	beer = Beer.objects.get(pk=pk)
	if request.method == 'POST':
		form = BeerForm(request.POST)
		if form.is_valid():
			beer.size = form.cleaned_data['size']
			beer.name = form.cleaned_data['name']
			beer.price = form.cleaned_data['price']
			beer.beer_type = form.cleaned_data['beer_type']
			beer.bottle_type = form.cleaned_data['bottle_type']
			beer.save()

			return redirect(beer)
	else:
		form = BeerForm(initial={'name': beer.name, 'size': beer.size, 'price': beer.price, 'beer_type': beer.beer_type, 'bottle_type': beer.bottle_type})

	return render(request, 'myapp/beer_update.html', {'form': form, 'beer_name': beer.name})

def ApiUpdateStore(request, pk):
	store = Store.objects.get(pk=pk)
	if request.method == 'POST':
		form = StoreForm(request.POST)
		if form.is_valid():
			store.inventory = form.cleaned_data['inventory']
			store.name = form.cleaned_data['name']
			store.location = form.cleaned_data['location']
			store.save()

			return redirect(store)

	else:
		form = StoreForm(initial={'name': store.name, 'inventory': store.inventory, 'location': store.location})

	return render(request, 'myapp/store_update.html', {'form': form, 'store_name': store.name})

def ApiUpdateOrder(request, pk):
	order = Order.objects.get(pk=pk)
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			order.buyer = form.cleaned_data['buyer']
			#order.buyer = request.user
			order.item = form.cleaned_data['item']
			order.save()

			return redirect(order)

	else:
		form = OrderForm(initial={'name': order.buyer, 'item': order.item})

	return render(request, 'myapp/order_update.html', {'form': form, 'order_buyer': order.buyer})

def ApiUpdateTrip(request, pk):
	trip = Trip.objects.get(pk=pk)
	if request.method == 'POST':
		form = TripForm(request.POST)
		if form.is_valid():
			#trip.runner = request.user
			trip.runner = form.cleaned_data['runner']
			trip.store = form.cleaned_data['store']
			trip.active = True
			trip.save()

			return redirect(trip)

	else:
		form = TripForm(initial={'runner': trip.runner, 'store': trip.store, 'active': trip.active})

	return render(request, 'myapp/trip_update.html', {'form': form, 'trip_runner': trip.runner})


