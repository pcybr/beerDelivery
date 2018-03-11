from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from myapp.models import Person, Beer, Store, Trip, Order
import os
import json
from django.core.management import call_command


class TestPerson(TestCase):

	def setUp(self):
		# os.system('python /app/beerDelivery/beerDelivery/manage.py loaddata db.json')
		call_command("loaddata", "/app/beerDelivery/beerDelivery/db.json")

		# Person.objects.create(name='Peter',age=20,person_id=200)
		
		pass #nothing to set up 

	def test_person_does_not_exist(self):
		response = self.client.get(reverse('person_get', args=['50']))
		resp = json.loads((response.content).decode("utf-8"))
		self.assertEquals(response.status_code, 200)
		self.assertEquals(resp['error'],404)

	def test_person_does_exist(self):
		response = self.client.get(reverse('person_get', kwargs = {'pk': 1}))
		resp = json.loads((response.content).decode("utf-8"))
		self.assertEquals(response.status_code, 200)
		self.assertEquals(resp['name'],'Pete')
		self.assertEquals(resp['age'],21)
		print(resp)

	#tearDown method is called after each test
	def tearDown(self):
		pass #nothing to tear down


