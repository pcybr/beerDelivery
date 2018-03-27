from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from myapp.models import Person, Beer, Store, Trip, Order, Authenticator
import os
import json
from django.core.management import call_command
from django.contrib.auth.hashers import make_password



class TestPerson(TestCase):

	def setUp(self):
		# os.system('python /app/beerDelivery/beerDelivery/manage.py loaddata db.json')
		# call_command("loaddata", "/app/beerDelivery/beerDelivery/db.json")

		Person.objects.create(name='Peter',age=20,person_id=200,username='Nic',password=make_password('nic'))
		
		pass #nothing to set up 

	def test_person_does_not_exist(self):
		response = self.client.get(reverse('person_get', args=['50']))
		resp = json.loads((response.content).decode("utf-8"))
		self.assertEquals(response.status_code, 200)
		self.assertEquals(resp['error'],404)

	def test_person_does_exist(self):
		response = self.client.get(reverse('person_get', args=['200']))
		resp = json.loads((response.content).decode("utf-8"))
		self.assertEquals(response.status_code, 200)
		self.assertEquals(resp['name'],'Peter')
		self.assertEquals(resp['age'],20)

	# def test_person_update(self):
	# 	response = self.client.post('/api/v1/person/200/update',{'name' : "Winston", 'age':21,'username':'Nic','password':'yes'})
	# 	response1 = self.client.get(reverse('person_get', args=['200']))
	# 	resp = json.loads((response1.content).decode("utf-8"))
	# 	self.assertEquals(response.status_code, 200)
	# 	self.assertEquals(resp['age'],21)
	# 	self.assertEquals(resp['name'],"Winston")

	# User Story 6
	def test_person_delete(self):
		response = self.client.post('/api/v1/person/200/delete')
		response1 = self.client.get(reverse('person_get', args=['200']))
		resp = json.loads((response1.content).decode("utf-8"))
		self.assertEquals(resp['error'],404)
		self.assertEquals(resp['message'],"Person does not exist")
		

	#tearDown method is called after each test
	def tearDown(self):
		pass #nothing to tear down
