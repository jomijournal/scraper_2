#utf8

from bs4 import BeautifulSoup
import re
import urllib.parse as urlparse

class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        #/faculty
        new_urls = set() 
        links = soup.find_all('a', href = re.compile(r".htm"))
        # print(links)

        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        #url
        res_data['url'] = page_url

        #<div id="bio-primary-contact"><p>Children's Healthcare of Atlanta </p><p itemprop="streetAddress">1405 Clifton Rd</p><p><span itemprop="addressLocality">Atlanta</span>, <span itemprop="addressRegion">Georgia</span> <span itemprop="postalCode">30322</span></p><p><strong>Phone: </strong><span itemprop="telephone">404-785-6670</span></p><p><strong>Email: </strong><a href="mailto:thomas.austin@emory.edu" itemprop="email">thomas.austin@emory.edu</a></p></div>
        # <a href="mailto:sryoung@emory.edu" itemprop="email">sryoung@emory.edu</a>
        if soup.find('article', class_="person") != None:
            name_node = soup.find('article', class_ = "person").find("h1")
            if name_node != None:
                res_data['name'] = name_node.get_text() 
                print(res_data['name'])

        if soup.find('div', id = 'bio-primary-contact') != None:
            email_node = soup.find('div', id = "bio-primary-contact").find("a")
            if email_node != None:
                res_data['email'] = email_node.get_text()
                print(res_data['email'])
        return res_data


    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding = 'utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data



        