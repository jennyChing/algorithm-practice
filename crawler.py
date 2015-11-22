import pandas as pd
#import splinter as sl
from splinter import Browser
#from selenium import webdriver
import time
from random import randint
#url.fill('q', 'XXXX')

data = pd.read_csv('HK SFDC.csv', encoding = 'utf-8')

urls = data['Search URL']
#print data['Search URL']
#print 'u'+ urls[0]
#print urls[1]
#print urls[10]
websiteData = data['Website']
df = pd.DataFrame(data)

browser = Browser('chrome')
for i in range(31,65):
	url = urls[i]
	browser.visit(url)
	if browser.find_by_css('cite').text:
		results = browser.find_by_css('cite').text
	else:
		results = 'none'
	websiteData[i] = results
	time.sleep(randint(1,5))
	df.to_csv('SFDC_result.csv', sep='\t', encoding='utf-8')
.r-iAz6ZJraZ13I