from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from myapp.models import Person, Beer, Store, Trip, Order, Authenticator
import json


class TestLogout(TestCase):

	def setUp(self):
		Person.objects.create(name='Peter',age=20,person_id=400,username='Nic',password='yes')
		Person.objects.create(name='Winston',age=20,person_id=200,username='Win',password='yes')
		self.client.post('/api/v1/login',{'username' : "Nic", 'password':'yes'})
		pass #nothing to set up 

	def test_good_logout(self):
		response = self.client.post('/api/v1/logout')
		self.assertEquals(response.status_code, 200)

	def test_bad_logout(self):
		#self.client.post('/api/v1/login',{'username' : "Nic", 'password':'yes'})
		self.client.post('/api/v1/logout')
		response = self.client.post('/api/v1/logout')
		self.assertEquals(response.status_code, 400)






	
	#tearDown method is called after each test
	def tearDown(self):
		pass #nothing to tear down