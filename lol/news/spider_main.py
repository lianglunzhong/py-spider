#conding:utf-8
import url_manager
import html_downloader
import html_parser
import ts_data

class SpiderMain(object):
	"""docstring for ClassName"""
	def __init__(self):
		super(SpiderMain, self).__init__()
		self.ts_url = 'http://127.0.0.1:8000/api/lol/save_news'
		self.urls = url_manager.UrlManager();
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.ts = ts_data.TsData(self.ts_url)


	def craw(self, root_urls):
		data = {}
		for root_url in root_urls:

			self.urls.add_new_url(root_url['url'])

			while self.urls.has_new_url():
				try:
					new_url = self.urls.get_new_url()
					html_cont = self.downloader.download(new_url)
					res_data = self.parser.parse(new_url, html_cont)
					data[root_url['name']] = res_data
				except Exception as e:
					print('craw faild')
					print(e)
		try:
			self.ts.save_data(data)
		except Exception as e:
			print(e)

if __name__ == "__main__":
	root_urls = [
		{
			'name': 'recom',
			'url': 'http://lol.qq.com/webplat/info/news_version3/152/4579/m5583/list_1.shtml'
		},
		{
			'name': 'govern',
			'url': 'http://lol.qq.com/webplat/info/news_version3/152/4579/4581/m5583/list_1.shtml'
		},
		{
			'name': 'sports',
			'url': 'http://lol.qq.com/webplat/info/news_version3/152/4579/4584/m5755/list_1.shtml'
		}
	]
	
	obj_spider = SpiderMain()
	obj_spider.craw(root_urls)
