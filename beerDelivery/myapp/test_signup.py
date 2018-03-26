from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from myapp.models import Person, Beer, Store, Trip, Order, Authenticator
import json


class TestSignup(TestCase):

	def setUp(self):
		Person.objects.create(name='Peter',age=20,person_id=200,username='Nic',password='yes')

		pass #nothing to set up 

	def test_good_signup(self):
		response = self.client.post('/api/v1/signup',{'username' : "JoJo", 'password':'yes', 'name':'Peter','age':20,'person_id':600})
		self.assertEquals(response.status_code, 200)

	def test_used_username(self):
		self.client.post('/api/v1/signup',{'username' : "Nic", 'password':'yes', 'name':'Peter','age':20,'person_id':800})
		response = self.client.post('/api/v1/signup',{'username' : "Nic", 'password':'yes', 'name':'Peter','age':20,'person_id':900})
		self.assertEquals(response.status_code, 400)

	
	#tearDown method is called after each test
	def tearDown(self):
		pass #nothing to tear down