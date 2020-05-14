# cmdEmailer.py - takes an email address and string of text on the command
# line and then, using Selenium, logs into your email account and
# sends an email of the string to the provided address.
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Firefox()

browser.get("https://mail.google.com/")
time.sleep(2)

userElem = browser.find_element_by_css_selector("#identifierId")
userElem.send_keys("xxx@gmail.com")
submitElem = browser.find_element_by_css_selector(".RveJvd")
submitElem.click()

time.sleep(2)

passElem = browser.find_element_by_css_selector(".I0VJ4d > div:nth-child(1) > input:nth-child(1)")
submitPassElem = browser.find_element_by_css_selector("#passwordNext > span:nth-child(3) > span:nth-child(1)")
passElem.send_keys("xxxx")
submitPassElem.click()

time.sleep(2)

writeElem = browser.find_element_by_css_selector(".T-I-KE")
writeElem.click()

time.sleep(4)

actions = ActionChains(browser)
actions.send_keys('mail_goes_here@mail.com')

actions.send_keys(Keys.TAB)
actions.send_keys(Keys.TAB)
actions.send_keys("Subject goes here")

actions.send_keys(Keys.TAB)
actions.send_keys("text goes here")

actions.send_keys(Keys.TAB)
actions.send_keys(Keys.ENTER)
actions.perform()