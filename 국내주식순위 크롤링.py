from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome()
TOP_50 = list()
url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page=1'
driver.get(url)

i = 2 #start index is 2

while(len(TOP_50) < 50):
    xpath_id = str('//*[@id="contentarea"]/div[3]/table[1]/tbody/tr[') + str(i) + str(']/td[2]/a')
    i+=1
    try:
        found = driver.find_element("xpath", xpath_id)
        #print(found.text)
        TOP_50.append(found.text)
    except:
        print("There is no xpath_id like that %s"%xpath_id)
print(TOP_50)
