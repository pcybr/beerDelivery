from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from myapp.models import Person, Beer, Store, Trip, Order
import os
import json
from django.core.management import call_command


class TestTrip(TestCase):

	def setUp(self):
		# os.system('python /app/beerDelivery/beerDelivery/manage.py loaddata db.json')
		# call_command("loaddata", "/app/beerDelivery/beerDelivery/db.json")

		Person.objects.create(name='Peter',age='20',person_id='200')
		Beer.objects.create(name='Bud Light',size=100,beer_id=1,bottle_type='Can',beer_type='Light',price=12)
		Store.objects.create(store_id=2,location='New York',inventory='Everything',name='Heaven')
		Order.objects.create(buyer='200',item=1,order_id='17')

		Trip.objects.create(trip_id='12',runner=200,store=2,active=True,orders=17)
		
		pass #nothing to set up 

	def test_trip_does_not_exist(self):
		response = self.client.get(reverse('trip_get', args=['50']))
		resp = json.loads((response.content).decode("utf-8"))
		self.assertEquals(response.status_code, 200)
		self.assertEquals(resp['error'],404)

	def test_trip_does_exist(self):
		response = self.client.get(reverse('trip_get', args=['12']))
		resp = json.loads((response.content).decode("utf-8"))
		self.assertEquals(response.status_code, 200)
		self.assertEquals(resp['buyer'].name,'Peter')
		

	#tearDown method is called after each test
	def tearDown(self):
		pass #nothing to tear down


