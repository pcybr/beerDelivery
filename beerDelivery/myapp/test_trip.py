from django.test import TestCase, Client
from django.core.urlresolvers import reverse
# from models import Person, Beer, Store, Trip, Order
from myapp.models import Person, Beer, Store, Trip, Order
import os
import json
from django.core.management import call_command


class TestTrip(TestCase):

	def setUp(self):
		# os.system('python /app/beerDelivery/beerDelivery/manage.py loaddata db.json')
		# call_command("loaddata", "/app/beerDelivery/beerDelivery/db.json")
		# Beer.objects.create(name='Bud Light',size=100,beer_id=1,bottle_type='Can',beer_type='Light',price=12)


		Trip.objects.create(trip_id=12,runner=Person.objects.create(name='Peter',age=20,person_id=200),store=Store.objects.create(store_id=2,location='New York',inventory='Everything',name='Heaven'),active=True)
		
		pass #nothing to set up 

	def test_trip_does_not_exist(self):
		response = self.client.get(reverse('trip_get', args=['50']))
		resp = json.loads((response.content).decode("utf-8"))
		self.assertEquals(response.status_code, 200)
		self.assertEquals(resp['error'],404)

	# User story 1
	def test_trip_does_exist(self):
		response = self.client.get(reverse('trip_get', args=['12']))
		resp = json.loads((response.content).decode("utf-8"))
		self.assertEquals(response.status_code, 200)
		self.assertEquals(resp['runner'],'Peter')
		self.assertEquals(resp['store'],'Heaven')
		self.assertEquals(resp['active'],True)


	# url(r'^api/v1/trip/(?P<pk>\d+)$', views.ApiTripGetView, name='trip_get'),
	# url(r'^api/v1/trip/create', views.ApiCreateTrip, name='trip_create'),
	# url(r'^api/v1/trip/(?P<pk>\d+)/delete$', views.ApiTripDeleteView, name='trip_delete'),
	# url(r'^api/v1/trip/(?P<pk>\d+)/update$', views.ApiUpdateTrip, name='trip_update'),

	# User story 2
	def test_trip_update(self):
		response = self.client.get(reverse('trip_get', args=['12']))
		resp = json.loads((response.content).decode("utf-8"))
		time = resp['time']
		store = Store.objects.get(store_id = 2)
		person = Person.objects.create(name='Winston',age=21,person_id=201)
		person.save()
		response1 = self.client.post('/api/v1/trip/12/update',{'runner' : 201, 'store':2, 'active': False})
		response3 = self.client.get(reverse('trip_get', args=['12']))
		resp3 = json.loads((response3.content).decode("utf-8"))
		self.assertEquals(resp3['runner'],'Winston')

	# User story 3
	def test_trip_update_status(self):
		response = self.client.get(reverse('trip_get', args=['12']))
		resp = json.loads((response.content).decode("utf-8"))
		time = resp['time']
		store = Store.objects.get(store_id = 2)
		response1 = self.client.post('/api/v1/trip/12/update',{'runner' : 200, 'store':2, 'active':False})
		response3 = self.client.get(reverse('trip_get', args=['12']))
		resp3 = json.loads((response3.content).decode("utf-8"))
		print(resp3)
		self.assertEquals(resp3['active'],False)

	# User story 4 can't be completed until Pete finishes

	def test_trip_delete(self):
		response = self.client.get(reverse('trip_get', args=['12']))
		trip = Trip.objects.get(pk=12)
		trip.delete()
		response = self.client.get(reverse('trip_get', args=['12']))
		resp = json.loads((response.content).decode("utf-8"))
		self.assertEquals(resp['error'],404)
		

	#tearDown method is called after each test
	def tearDown(self):
		pass #nothing to tear down


