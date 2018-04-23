from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import unittest
import os

# filepath = os.path.join('c:/Users/peter/Downloads', 'chromedriver')
# if not os.path.exists('c:/Users/peter/Downloads'):
#     os.makedirs('c:/Users/peter/Downloads')
# f = open(filepath, "chromedriver")

class web_tests(unittest.TestCase):
	def test_login(self):
		# driver = webdriver.Chrome("c:/Users/peter/Downloads/chromedriver")
		driver = webdriver.Remote(
		command_executor='http://selenium-chrome:4444/wd/hub',
		desired_capabilities=DesiredCapabilities.CHROME)

		driver.get("http://web:8000/login/")
		username = driver.find_element_by_id("id_username")
		username.send_keys('pete')
		password = driver.find_element_by_id('id_password')
		password.send_keys('pete')
		driver.find_element_by_id('login').click()
		welcome = driver.find_element_by_id('welcome')
		if "Welcome to Goombay Smash Beer Delivery!" == welcome:
			assert True
		driver.quit()

	def test_create_trip(self):
		driver = webdriver.Remote(
		command_executor='http://selenium-chrome:4444/wd/hub',
		desired_capabilities=DesiredCapabilities.CHROME)		
		driver.get("http://web:8000/login/")
		username = driver.find_element_by_id("id_username")
		username.send_keys('pete')
		password = driver.find_element_by_id('id_password')
		password.send_keys('pete')
		driver.find_element_by_id('login').click()
		driver.find_element_by_id('createTrip').click()
		driver.find_element_by_id('createTripButton').click()
		welcome = driver.find_element_by_id('welcome')
		if "Welcome to Goombay Smash Beer Delivery!" == welcome:
			assert True
		driver.quit()


	def test_search(self):
		driver = webdriver.Remote(
		command_executor='http://selenium-chrome:4444/wd/hub',
		desired_capabilities=DesiredCapabilities.CHROME)		
		driver = webdriver.Remote(
		command_executor='http://selenium-chrome:4444/wd/hub',
		desired_capabilities=DesiredCapabilities.CHROME)		
		driver.get("http://web:8000/signup/")
		name = driver.find_element_by_id("id_name")
		name.send_keys('tester_pete')
		age = driver.find_element_by_id("id_age")
		age.send_keys(22)
		username = driver.find_element_by_id("id_username")
		username.send_keys('tester_pete')
		password = driver.find_element_by_id('id_password')
		password.send_keys('tester_pete')
		driver.find_element_by_id("button").click()
		driver.find_element_by_id('login').click()
		driver.find_element_by_id('createTrip').click()
		driver.find_element_by_id('createTripButton').click()

		search = driver.find_element_by_id('navSearch')
		search.send_keys('tester_pete')
		driver.find_element_by_id("navSearchSubmit").click()
		result = driver.find_element_by_id("matchingTrips")
		if result == "Matching Trips:":
			assert True
		driver.quit()

	def test_signup(self):
		driver = webdriver.Remote(
		command_executor='http://selenium-chrome:4444/wd/hub',
		desired_capabilities=DesiredCapabilities.CHROME)		
		driver.get("http://web:8000/signup/")
		name = driver.find_element_by_id("id_name")
		name.send_keys('tester')
		age = driver.find_element_by_id("id_age")
		age.send_keys(22)
		username = driver.find_element_by_id("id_username")
		username.send_keys('tester')
		password = driver.find_element_by_id('id_password')
		password.send_keys('tester')
		driver.find_element_by_id("button").click()
		welcome = driver.find_element_by_id('welcome')
		if "Welcome to Goombay Smash Beer Delivery!" == welcome:
			assert True
		driver.quit()







	# def tearDown(self):
	# 	self.driver.close()

if __name__ == "__main__":
	unittest.main()

# Create your tests here.
