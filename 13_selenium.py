import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 

browser = webdriver.Chrome("/Users/jaeyeol/jaeyeol/python/chromedriver")
browser.get("http://naver.com")

# elem = browser.find_element_by_class_name("link_login ")
# elem.click()

# elem = browser.find_element_by_id("query")
# elem.send_keys("이재열")
# elem.send_keys(Keys.ENTER)

# elem = browser.find_elements_by_tag_name("a")
# for e in elem:
#   e.get_attribute("href")  

elem = browser.find_element_by_class_name("link_login")
elem.click()
browser.find_element_by_id("id").send_keys("gaedol9185")
browser.find_element_by_id("pw").send_keys("1023qwer!")
browser.find_element_by_id("log.login").click()


