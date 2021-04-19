from time import sleep
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.instagram.com")
sleep(4)
driver.find_element_by_xpath("//input[@name=\"username\"]")\
    .send_keys("your username")
driver.find_element_by_xpath("//input[@name=\"password\"]")\
    .send_keys("your password")
driver.find_element_by_xpath('//button[@type="submit"]')\
    .click()
sleep(4)
#################################################
#type your username in place of  'your username'#
#################################################
driver.get("https://www.instagram.com/your username/")
following=driver.find_element_by_partial_link_text("following")
following.click()

sleep(5)
for i in range(5):
    driver.find_element_by_xpath('//button[text()="Following"]')\
        .click()
    driver.find_element_by_xpath('//button[text()="unfollow"]')\
        .click()
        sleep(2)