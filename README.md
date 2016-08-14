# proxy2fs
Makes a static local cache of all web resources which flow through mitmproxy.

# Ubuntu mitmproxy Install

```
sudo apt-get install python-pip python-dev libffi-dev libssl-dev
sudo apt-get install libxml2-dev libxslt1-dev libjpeg8-dev zlib1g-dev
sudo pip install mitmproxy
```

# Start it up
```
mitmproxy -s "proxy2fs.py cacheDir/"
```

# Connect to it with PhantomJS
```
phantomjs --ignore-ssl-errors=yes --proxy=localhost:8080 "rasterize.js" "https://www.google.com"
```
# Note

This will only work with HTTPS if the web browser is set to ignore the HTTPS errors.

# Credits

Author: Wes Turner

License: MIT License
