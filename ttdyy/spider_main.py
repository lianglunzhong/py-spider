#coding:utf-8
import url_manager

class SpiderMain(object):
	"""docstring for ClassName"""
	def __init__(self):
		super(SpiderMain, self).__init__()

		self.pageUrl = url_manager.PageUrlManager()
		self.movieUrl = url_manager.MovieUrlManager()
		self.movie = url_manager.MovieManager()


	def craw(self, root_url):
		page_urls = self.pageUrl.get_page_urls(root_url)
		# for page_url in page_urls:
		# 	self.movieUrl.get_page_movie_urls(page_url)
		self.movieUrl.get_page_movie_urls("http://www.dytt8.net/html/gndy/dyzz/list_23_1.html")

		movie_urls = self.movieUrl.get_all_movie_urls()
		for movie_url in movie_urls:
			movie_data = self.movie.get_movie_data(movie_url)



if __name__ == '__main__':
	root_url = "http://www.dytt8.net/html/gndy/dyzz/list_23_1.html"
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)
