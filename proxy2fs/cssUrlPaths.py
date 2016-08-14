"""
Downloads files mentioned in CSS file and converts paths relative to document root
"""

try:
	from urlparse import urljoin, urlparse  # Python2
except ImportError:
	from urllib.parse import urljoin, urlparse  # Python3

import re
import errno
import os
import urllib

base_url = 'http://www.asite.com'
 
import os

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

with open('cache/css.css', 'r') as myfile:
	data = myfile.read()
	for cssurl in re.findall('url\(([^)]+)\)', data):
		fullurl = urljoin(base_url, cssurl)
		docpath = urlparse(fullurl).path
		data = re.sub(cssurl, docpath, data)
		filepath = os.getcwd()+"/cache"+docpath
		exists = os.path.isfile(filepath)
		if not exists:
			print "Downloading"
			mkdir_p(os.path.dirname(filepath))
			urllib.urlretrieve (fullurl, filepath)
		else:
			print "Already exists!"
	#print data
