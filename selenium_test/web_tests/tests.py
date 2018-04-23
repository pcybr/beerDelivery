from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import unittest
from django.test import TestCase, Client


class web_tests(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Remote(
		command_executor='http://127.0.0.1:4444/wd/hub',
		desired_capabilities=DesiredCapabilities.CHROME)

    # def test_search_person(self):
    #     driver = self.driver
    #     driver.get("http://localhost:8003/")
    #     self.assertIn("Goombay", driver.title)
    #     elem = driver.find_element_by_name("q")
    #     elem.send_keys("pycon")
    #     elem.send_keys(Keys.RETURN)
    #     assert "No results found." not in driver.page_source
	def test_login(self):
		driver = self.driver
		driver.get("http://web:8000/login/")
		print(driver.current_url)
		username = driver.find_element_by_id("id_username")
		username.send_keys('pete')
		password = driver.find_element_by_id('id_password')
		password.send_keys('pete')
		driver.find_element_by_xpath('//input[@value = "Submit"]').click()
		driver.quit()

	# def test_search(self):
	# 	driver = self.driver
	# 	driver.get("http://127.0.0.1:8003/login/")
	# 	print(driver.current_url)
	# 	username = driver.find_element_by_id("id_username")
	# 	username.send_keys('pete')
	# 	password = driver.find_element_by_id('id_password')
	# 	password.send_keys('pete')
	# 	driver.find_element_by_xpath('//input[@value = "Submit"]').click()

	# 	search = driver.find_element_by_id('navSearch')
	# 	search.send_keys('pete')
	# 	driver.find_element_by_id("navSearchSubmit").click()
	# 	driver.




	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()
