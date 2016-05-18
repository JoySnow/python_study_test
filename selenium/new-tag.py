from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://baidu.com/")

body = driver.find_element_by_tag_name("body")
body.send_keys(Keys.CONTROL + 't')
driver.get("http://web.qq.com")
sleep(10)


driver.close()
