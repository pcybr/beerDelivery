from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from myapp.models import Person, Beer, Store, Trip, Order
import os
import json
from django.core.management import call_command


class TestBeer(TestCase):

	def setUp(self):
		# os.system('python /app/beerDelivery/beerDelivery/manage.py loaddata db.json')
		# call_command("loaddata", "/app/beerDelivery/beerDelivery/db.json")

		Beer.objects.create(name='Bud Light',size=100,beer_id=1,bottle_type='Can',beer_type='Light',price=12)

		pass #nothing to set up 

	def test_beer_does_not_exist(self):
		response = self.client.get(reverse('beer_get', args=['100']))
		resp = json.loads((response.content).decode("utf-8"))
		self.assertEquals(response.status_code, 200)
		self.assertEquals(resp['error'],404)

	def test_beer_does_exist(self):
		response = self.client.get(reverse('beer_get', args=['1']))
		resp = json.loads((response.content).decode("utf-8"))
		self.assertEquals(response.status_code, 200)
		self.assertEquals(resp['name'],'Bud Light')
		

	#tearDown method is called after each test
	def tearDown(self):
		pass #nothing to tear down


