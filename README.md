# med-crawler
Med-crawler is a project during my internship in a medical education platform company. It helps to collect the target users from medical schools.

Python packages: 
-urllib2
-beautifulsoup 

Instructions:
This crawler includes 4 parts, the url manager, parser, downloader and outper. Also the main function is used to control the requeting numbers and the root url. 

The main url(root url) is inputted under main.py, line 38 under the main call.
Parser should be modified according to the web structure of the root url page. For instance, 'soup.find('div', id = "bio-primary-contact").find("a")' will help you to find all the hyperlinks with the id of 'bio-primary-contact'. For the institution pages, the structures are similar. 

