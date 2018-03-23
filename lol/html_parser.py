#coding:utf-8
from bs4 import BeautifulSoup
import re
# import urlparse
import urllib.parse
import html_downloader

class HtmlParser(object):
	"""docstring for HtmlParser"""
	def __init__(self):
		super(HtmlParser, self).__init__()

		self.downloader = html_downloader.HtmlDownloader()
		
	def parse(self, page_url, html_cont):
		if page_url is None or html_cont is None:
			return

		soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
		# new_urls = self._get_new_urls(page_url, soup)
		# new_data = self._get_new_data(page_url, soup)
		datas = self._get_article_data(page_url, soup)
		return datas


	def _get_new_urls(self, page_url, soup):
		new_urls = set()
		# /item/
		links = soup.find_all('a', href=re.compile(r"/item/"))

		for link in links:
			new_url = link['href']
			new_full_url = urllib.parse.urljoin(page_url, new_url)
			new_urls.add(new_full_url)

		return new_urls


	def _get_new_data(self, page_url, soup):
		res_data = {}
		#<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
		title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
		res_data['title'] = title_node.get_text().encode("utf-8")

		#<div class="lemma-summary" label-module="lemmaSummary">
		summary_node = soup.find('div', class_='lemma-summary')
		res_data['summary'] = summary_node.get_text().encode("utf-8")

		#url
		res_data['url'] = page_url

		return res_data

	def _get_article_data(self, page_url, soup):
		datas = []

		articles = soup.find_all('li', 'news-lst')

		for article in articles:
			data = {}
			lnk = article.find('a', 'lnk-type').get_text()
			date = article.find('span', 'date').get_text()
			title = article.find('a', 'lnk-type').next_sibling.get_text()

			data['lnk'] = lnk
			data['date'] = date
			data['title'] = title

			article_url = article.find('a', 'lnk-type').next_sibling['href']
			article_url = urllib.parse.urljoin(page_url, article_url)
			html_cont = self.downloader.download(article_url)

			content = self._parseContent(html_cont)

			data['content'] = content

			datas.append(data)
		return datas

	def _parseContent(self, html_cont):
		if html_cont is None:
			return

		soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
		content = self._get_article_content(soup)
		return content

	def _get_article_content(self, soup):
		return 'this is content'
