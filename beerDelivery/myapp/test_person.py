from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from myapp.models import Person
import os
import json


class TestPerson(TestCase):

	def setUp(self):
		os.system('python /app/beerDelivery/beerDelivery/manage.py loaddata db.json')
		pass #nothing to set up 

	def test_person_does_not_exist(self):
		 #assumes user with id 1 is stored in db
		response = self.client.get(reverse('person_get', args=['50']))
		resp = json.loads((response.content).decode("utf-8"))
		self.assertEquals(response.status_code, 200)
		self.assertEquals(resp['error'],404)
		print(resp)
		print('-------')
		print(response.content)

		#checks that response contains parameter order list & implicitly
		# checks that the HTTP status code is 200
		# self.assertContains(response, 'order_list')

	#tearDown method is called after each test
	def tearDown(self):
		pass #nothing to tear down
