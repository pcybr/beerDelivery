from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from myapp.models import Person, Beer, Store, Trip, Order, Authenticator
import os
import json
from django.contrib.auth.hashers import make_password
from django.core.management import call_command


class TestLogout(TestCase):

	def setUp(self):
		Person.objects.create(name='Peter',age=20,person_id=200,username='Nic',password=make_password('nic'))
		Authenticator.objects.create(auth = "Peter",name='Peter',user_id=200)
		
		pass #nothing to set up 

	def test_good_logout(self):
		self.client.post('/api/v1/login',{'username' : "Nic", 'password':make_password('nic'),'auth_cookie':'Peter'})
		response = self.client.post('/api/v1/logout')
		resp = json.loads((response.content).decode("utf-8"))
		self.assertEquals(resp['status'], 400)

	def test_bad_logout(self):
		self.client.post('/api/v1/logout')
		response = self.client.post('/api/v1/logout')
		resp = json.loads((response.content).decode("utf-8"))
		self.assertEquals(resp['status'], 400)






	
	#tearDown method is called after each test
	def tearDown(self):
		pass #nothing to tear down