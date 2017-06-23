#utf8
from bs4 import BeautifulSoup
class HtmlParser(object):

	def paser(self, page_url, html_cont):
		if page_url is None or html_cont is None:
			return

		soup = BeautifulSoup(html_cont, 'html.parser', from_encoding = 'utf-8')


		