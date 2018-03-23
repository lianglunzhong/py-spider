import urllib2, cookielib
import bs4
import re
from bs4 import BeautifulSoup

html_doc = """
<select name="sldd" style="width:78" onchange="location.href=this.options[this.selectedIndex].value;">
<option value="list_23_1.html">1</option>
<option value="list_23_2.html">2</option>
<option value="list_23_3.html">3</option>
<option value="list_23_4.html">4</option>
<option value="list_23_5.html">5</option>
<option value="list_23_6.html">6</option>
<option value="list_23_7.html">7</option>
<option value="list_23_8.html">8</option>
</select>
"""

soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

print 'lalala'
links = soup.find('select', attrs={"name": "sldd"}).find_all('option')
for link in links:
	print link['value']


# print 'zheng ze pi pei'
# link_node = soup.find('a', href=re.compile(r'ill'))
# print link_node.name, link_node['href'], link_node.get_text()



# print 'huo qu p'
# p_node = soup.find('p', class_='title')
# print p_node.name, p_node.get_text()