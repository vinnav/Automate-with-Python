from selenium import webdriver

browser = webdriver.Firefox()

browser.get("https://automatetheboringstuff.com")

elem = browser.find_element_by_css_selector(".top_header > a:nth-child(3)")

elem.click()

# browser.back()
# browser.forward()
# browser.refresh()
# browser.quit()
