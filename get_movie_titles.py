import requests 
import datetime
from lxml import html
from lxml.etree import tostring

START_YEAR = '2014'
END_YEAR = '2018'
movieYear = START_YEAR

for i in range(int(END_YEAR) - int(START_YEAR)):
	IMDBUrl = 'https://www.imdb.com/search/title?year=' + movieYear + '&title_type=feature&'


	imdbMoviePage = requests.get(IMDBUrl)

	#Movie page is now in a tree an accessible with xpath
	movieTree = html.fromstring(imdbMoviePage.content)

	movieHeaders= movieTree.xpath('//h3[@class="lister-item-header"]')

	#Write movies to csv
	fileStream = open("movieTitles.txt", "a+")
	for header in movieHeaders:

		headerStr = html.tostring(header, encoding='unicode')
		startIndex = headerStr.index('/">')
		endIndex = headerStr.index('</a>')
		
		headerTitle = headerStr[startIndex + 3 : endIndex]
		
		fileStream.write(headerTitle + '\n')
	fileStream.close()	

	movieYear = str(int(movieYear) + 1)
	

