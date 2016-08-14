# proxy2fs
Makes a static local cache of all web resources which flow through mitmproxy.

# Ubuntu mitmproxy Install

```
sudo apt-get install python-pip python-dev libffi-dev libssl-dev
sudo apt-get install libxml2-dev libxslt1-dev libjpeg8-dev zlib1g-dev
sudo pip install mitmproxy
```

# Usage
```
mitmproxy -s "proxy2fs.py cacheDir/"
```

# Credits

Author: Wes Turner

License: MIT License
