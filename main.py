#utf8

import url_manager
import html_downloader
import html_parser
import html_outputer

class SpiderMain(object):
	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()

	def craw(self, root_url):
		count = 1
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			try:
				new_url = self.urls.get_new_url()
				# print(new_url)
				print(count)
				html_cont = self.downloader.download(new_url)
				new_urls, new_data = self.parser.parse(new_url, html_cont)
				self.urls.add_new_urls(new_urls)
				self.outputer.collect_data(new_data)
				count += 1

				if count == 500:
					break

			except:
				print('failed')

		self.outputer.output_html()


if __name__ == '__main__':
	root_url = 'http://www.anesthesiology.emory.edu/faculty/index.html'
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)