from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

#browser.get('http://www.baidu.com')
browser.get('http://www.topuniversities.com/university-rankings/world-university-rankings/2015#sorting=rank+region=+country=+faculty=+stars=false+search=')
print "got the page ..."

content = browser.page_source
print "type: ", type(content)
print content

#browser.quit()
