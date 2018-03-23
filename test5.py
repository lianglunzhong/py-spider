#coding:utf-8
import urllib2
from bs4 import BeautifulSoup
import re

url = 'http://www.ygdy8.com/html/gndy/jddy/20170924/55099.html'

request = urllib2.Request(url)
request.add_header('user-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13 ')

response = urllib2.urlopen(request)

if response.getcode() != 200:
	print 'urlopen failed'
	exit()

html_doc = response.read()

soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

links = soup.find('div', class_='co_area2').find('div', class_='co_content2').find('ul').find_all('a', attrs={'href':re.compile(r"/html/gndy/dyzz/"),'class':'ulink'})


fout = open('test2.txt', 'w')

for link in links:
	fout.write('http://www.dytt8.net' + link['value'] + '\r\n')

fout.close()