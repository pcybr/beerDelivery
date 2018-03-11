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

		
		# Beer.objects.create(name='Bud Light',size=100,beer_id=1,bottle_type='Can',beer_type='Light',price=12)
		
		

		Trip.objects.create(trip_id=12,runner=Person.objects.create(name='Peter',age=20,person_id=200),store=Store.objects.create(store_id=2,location='New York',inventory='Everything',name='Heaven'),active=True)
		
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
		self.assertEquals(resp['runner'],'Peter')
		self.assertEquals(resp['store'],'Heaven')
		self.assertEquals(resp['active'],True)
		

	#tearDown method is called after each test
	def tearDown(self):
		pass #nothing to tear down


