#coding:utf-8
import urllib2
from bs4 import BeautifulSoup

url = 'http://www.dytt8.net/html/gndy/dyzz/'

request = urllib2.Request(url)
request.add_header('user-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13 ')

response = urllib2.urlopen(request)

if response.getcode() != 200:
	print 'urlopen failed'
	exit()

html_doc = response.read()

soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

links = soup.find('select', attrs={"name": "sldd"}).find_all('option')

fout = open('test.txt', 'w')

for link in links:
	fout.write(url + link['value'] + '\r\n')

fout.close()