import requests
from lxml import html
from lxml.etree import tostring

def get_video_captions(video_id):

	CAPTION_URL = 'https://www.diycaptions.com/php/get-automatic-captions-as-txt.php?id='+video_id+'&language=asr'

	captionPage = requests.get(CAPTION_URL)
	captionTree = html.fromstring(captionPage.content)
	caption = captionTree.xpath('//div[@contenteditable="true"]/text()')

	return(str(caption))

if (__name__ == '__main__'):
	print(get_video_captions("RZjh_UsPZWk"))



