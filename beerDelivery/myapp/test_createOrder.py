from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from myapp.models import Person, Beer, Store, Trip, Order, Authenticator
import os
import json
from django.core.management import call_command


class TestCreateTrip(TestCase):

	def setUp(self):
		Person.objects.create(name = 'Peter', age = 20, person_id = 200, username = 'Nic', password = 'yes')
		Beer.objects.create(name='booze',size=100,beer_id=1,bottle_type='Can',beer_type='Light',price=12)
		pass #nothing to set up 

	def test_createOrder_good(self):
		response = self.client.post('/api/v1/createOrder',{'name': 'Peter', 'beer': "booze"})
		resp = json.loads((response.content).decode("utf-8"))
		self.assertEquals(resp['status'], 200)

	def test_createOrder_bad(self):
		response = self.client.post('/api/v1/createOrder',{'name': 'Peter', 'beer': "booooooze"})
		resp = json.loads((response.content).decode("utf-8"))
		self.assertEquals(resp['status'], 400)

	
	#tearDown method is called after each test
	def tearDown(self):
		pass #nothing to tear down