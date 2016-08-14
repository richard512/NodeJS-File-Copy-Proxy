"""
Opens an HTML file and replaces all IMG SRC paths with absolute paths
"""

try:
	from urlparse import urljoin, urlparse  # Python2
except ImportError:
	from urllib.parse import urljoin, urlparse  # Python3
from bs4 import BeautifulSoup

base_url = 'http://www.asite.com'

with open('cache/index.html', 'r') as myfile:
	data = myfile.read()
	soup = BeautifulSoup(data, "lxml")

	for img in soup.find_all('img', src=True):
		src = img.get('src')
		src = urljoin(base_url, src)
		docpath = urlparse(src).path
		img['src'] = docpath
		#print(docpath)
	print soup
