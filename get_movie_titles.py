import requests 
import datetime
from lxml import html
from lxml.etree import tostring

imdbMoviePage = requests.get('https://www.imdb.com/search/title?year=2018&title_type=feature&')

#Movie page is now in a tree an accessible with xpath
movieTree = html.fromstring(imdbMoviePage.content)

movieHeaders= movieTree.xpath('//h3[@class="lister-item-header"]')

#Write movies to csv
fileStream = open("movieTitles.csv", "w+")
for header in movieHeaders:

	headerStr = html.tostring(header, encoding='unicode')
	startIndex = headerStr.index('/">')
	endIndex = headerStr.index('</a>')
	
	headerTitle = headerStr[startIndex + 3 : endIndex]
	
	fileStream.write(headerTitle + '\n')

