# med-crawler
Med-crawler is a project during my internship in a medical education platform company. It helps to collect the target users from medical schools.

Python packages: 
-urllib2
-beautifulsoup 

Instructions:
This crawler includes 4 parts, the url manager, parser, downloader and outper. Also the main function is used to control the requeting numbers and the root url. 

The main url(root url) is inputted under main.py, line 38 under the main call.

The downloader will download the requested url automatically and extract all the contents. 

Parser should be modified according to the web structure of the root url page. For instance, 'soup.find('div', id = "bio-primary-contact").find("a")' will help you to find all the hyperlinks with the id of 'bio-primary-contact'. For the institution pages, the structures are similar. 


[![Capture.jpg](https://s26.postimg.org/gc0tbbq0p/Capture.jpg)](https://postimg.org/image/tg6do0i2d/)


In outputer, the data is finally analyzed and generated. The format can be adjusted in csv or html file. 


