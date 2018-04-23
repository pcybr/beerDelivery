from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys


browser = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.CHROME)

browser.get("http://www.python.org")
assert "Python" in browser.title
if "Python" in browser.title:
    print("Python is in the browser title!")
else:
    print("Failed to get correct title.")
elem = browser.find_element_by_name("q")
print(elem)
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in browser.page_source
browser.close()
print("HELLO MADE IT HERE LUV")
browser.quit()