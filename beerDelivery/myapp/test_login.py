from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from myapp.models import Person, Beer, Store, Trip, Order, Authenticator
import os
from django.contrib.auth.hashers import make_password
import json
from django.core.management import call_command


class TestLogin(TestCase):

	def setUp(self):
		Person.objects.create(name='Peter',age=20,person_id=200,username='Nic',password= make_password('nic'))
		pass #nothing to set up 

	def test_good_login(self):
		response = self.client.post('/api/v1/login',{'username' : "Nic", 'password':"nic"})
		resp = json.loads((response.content).decode("utf-8"))
		self.assertEquals(resp['status'], 200)

	def test_bad_password(self):
		response = self.client.post('/api/v1/login',{'username' : "Nic", 'password':'no'})
		resp = json.loads((response.content).decode("utf-8"))
		self.assertEquals(resp['status'], 400)

	def test_bad_username(self):
		response = self.client.post('/api/v1/login',{'username' : "NotNic", 'password':'yes'})
		resp = json.loads((response.content).decode("utf-8"))
		self.assertEquals(resp['status'], 404)

	
	#tearDown method is called after each test
	def tearDown(self):
		pass #nothing to tear down