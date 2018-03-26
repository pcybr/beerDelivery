from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from myapp.models import Person, Beer, Store, Trip, Order, Authenticator
import json


class TestLogin(TestCase):

	def setUp(self):
		Person.objects.create(name='Peter',age=20,person_id=200,username='Nic',password='yes')
		pass #nothing to set up 

	def test_good_login(self):
		response = self.client.post('/api/v1/login',{'username' : "Nic", 'password':'yes'})
		self.assertEquals(response.status_code, 200)

	def test_bad_password(self):
		response = self.client.post('/api/v1/login',{'username' : "Nic", 'password':'no'})
		self.assertEquals(response.status_code, 400)

	def test_bad_username(self):
		response = self.client.post('/api/v1/login',{'username' : "NotNic", 'password':'yes'})
		self.assertEquals(response.status_code, 404)

	
	#tearDown method is called after each test
	def tearDown(self):
		pass #nothing to tear down