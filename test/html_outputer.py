#coding:utf-8
#

class HtmlOutputer(object):
	"""docstring for html_outputer"""
	def __init__(self):
		super(HtmlOutputer, self).__init__()

		self.datas = []
		
	def collect_data(self, data):
		if data is None:
			return

		self.datas.append(data)

	def output_html(self):
		fout = open('output.html', 'w')

		fout.write('<html>')
		fout.write('<body>')
		fout.write('<table>')

		#ascii
		for data in self.datas:
			fout.write('<tr>')
			fout.write('<td>%s</td>' %data['url']) 
			fout.write('<td>%s</td>' %data['title']) 
			fout.write('<td>%s</td>' %data['summary']) 
			fout.write('</tr>')

		fout.write('</table>')
		fout.write('</body>')
		fout.write('</html>')

		fout.close()