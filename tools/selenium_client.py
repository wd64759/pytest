from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = "D:/workroom/code100/webdriverio/chromedriver.exe"

driver = webdriver.Chrome(chromedriver)
driver.get("http://www.baidu.com")

elem = driver.find_element_by_id("kw")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
print(driver.page_source)
driver.close()