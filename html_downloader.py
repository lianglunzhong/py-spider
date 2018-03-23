#coding:utf-8
import urllib2

class HtmlDownloader(object):
	"""docstring for HtmlDownloader"""
	def __init__(self):
		super(HtmlDownloader, self).__init__()
		
	def download(self, url):
		if url is None:
			return None

		request = urllib2.Request(url)
		request.add_header('user-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13 ')

		response = urllib2.urlopen(request)

		if response.getcode() != 200:
			return None

		return response.read()
