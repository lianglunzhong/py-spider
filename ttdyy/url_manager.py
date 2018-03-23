#coding:utf-8
import html_downloader
from bs4 import BeautifulSoup
import re

class PageUrlManager(object):
	"""docstring for PageUrlManager"""
	def __init__(self):
		super(PageUrlManager, self).__init__()
		
		self.downloader = html_downloader.HtmlDownloader()
		self.page_urls = set()

	def get_page_urls(self, root_url):
		html_doc = self.downloader.download(root_url)

		if html_doc:
			self.parse_page_urls(html_doc)

		return self.page_urls


	def parse_page_urls(self, html_doc):
		soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

		links = soup.find('select', attrs={"name": "sldd"}).find_all('option')

		mail_url = 'http://www.dytt8.net/html/gndy/dyzz/'

		for link in links:
			full_url = mail_url + link['value']

			self.page_urls.add(full_url)




class MovieUrlManager(object):
	"""docstring for MovieUrlManager"""
	def __init__(self):
		super(MovieUrlManager, self).__init__()

		self.downloader = html_downloader.HtmlDownloader()
		self.movie_urls = set()


	def get_page_movie_urls(self, page_url):
		html_doc = self.downloader.download(page_url)

		if html_doc:
			self.parse_page_movie_urls(html_doc)


	def parse_page_movie_urls(self,html_doc):
		soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

		try:
			# links = soup.find('div', class_='co_content8')
			links = soup.find('div', class_='co_content8').find_all('a', attrs={'href':re.compile(r"/html/gndy/dyzz/"),'class':'ulink'})

			mail_url = 'http://www.dytt8.net'

			for link in links:
				full_url = mail_url + link['href']

				self.movie_urls.add(full_url)

		except Exception as e:
			print e

	def get_all_movie_urls(self):
		return self.movie_urls





class MovieManager(object):
	"""docstring for MovieManager"""
	def __init__(self):
		super(MovieManager, self).__init__()

		self.downloader = html_downloader.HtmlDownloader()
		self.movie_data = {}

	def get_movie_data(self, movie_url):
		html_doc = self.downloader.download(movie_url)

		if html_doc:
			self.parse_page_movie_urls(html_doc)
		
