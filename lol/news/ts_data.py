#coding:utf-8
import urllib.request
import urllib.parse
import json
import codecs

class TsData(object):
	"""docstring for TsData"""
	def __init__(self, url):
		super(TsData, self).__init__()
		self.url = url
		
	def tuisong_data(self, data):
		data = bytes(urllib.parse.urlencode(data), encoding="utf8")

		req = urllib.request.Request(url=self.url, data=data, method="POST")

		response = urllib.request.urlopen(req)

		if response.getcode() == 200:
			print('ts success')
		else:
			print('ts failed')

	def save_data(self, data):
		try:
			file = codecs.open('lol_news_data.json', 'w', 'utf-8')
			data = json.dumps(data, ensure_ascii=False, indent=2)
			file.write(data)
			file.close()
			print('save data success')
		except Exception as e:
			print(e)


