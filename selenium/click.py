#coding=utf-8

from selenium import webdriver
import time

browser = webdriver.Firefox()

first_url = 'https://www.timeshighereducation.com/world-university-rankings/2016/world-ranking#!/page/0/length/25/sort_by/rank_label/sort_order/asc/cols/scores'
print "now access %s" %(first_url)
browser.get(first_url)
select_all = browser.find_element_by_xpath("/html/body/div[6]/div/section/div/section/div/div/div[1]/div/div[1]/div/div/div[2]/div/div[4]/label/select/option[5]")

print select_all
print type(select_all)

select_all.click()

time.sleep(5)


#browser.quit()
