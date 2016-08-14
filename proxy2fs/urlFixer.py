"""
Resolves relative url paths to absolute paths
---
Example:
Input 1: "http://www.asite.com/folder/currentpage.html"
Input 2: "../scripts/jquery.js"
Output: "http://www.asite.com/scripts/jquery.js"
Output, parsed: "/scripts/jquery.js"
"""

try:
    from urlparse import urljoin, urlparse  # Python2
except ImportError:
    from urllib.parse import urljoin, urlparse  # Python3

CurrentPageURL = "http://www.asite.com/folder/currentpage.html"
print ""
print "CurrentPageURL: "+CurrentPageURL

samedir = urljoin(CurrentPageURL, "anotherpage.html")
deeperdir = urljoin(CurrentPageURL, "folder2/anotherpage.html")
absdir = urljoin(CurrentPageURL, "/folder3/anotherpage.html")
backdir = urljoin(CurrentPageURL, "../scripts/jquery.js")

print ""
print "The whole shebang:"
print samedir
print deeperdir
print absdir
print backdir

samedir = urlparse(samedir).path
deeperdir = urlparse(deeperdir).path
absdir = urlparse(absdir).path
backdir = urlparse(backdir).path

print ""
print "Relative to document root:"
print samedir
print deeperdir
print absdir
print backdir

print ""
