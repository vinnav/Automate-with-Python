from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Firefox()

browser.get("https://play2048.co/")
actions = ActionChains(browser)

for i in range(1,100):
    actions.send_keys(Keys.RIGHT)
    actions.send_keys(Keys.DOWN)
    actions.send_keys(Keys.LEFT)
    actions.send_keys(Keys.UP)
    actions.perform()