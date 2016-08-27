import re
from sys import exit, argv
from random import random
try:
    # Python 2.6-2.7
    from HTMLParser import HTMLParser
    import urllib2 as urllib
except ImportError:
    # Python 3
    from html.parser import HTMLParser
    import urllib.request as urllib

URL = "http://www.barzellette.net/"
SEZIONE = "leggi-di-murphy.html"
REGEX = '(?<=class="leggi-tutto"><\/a>)[\n\s\S]*?(?=<\/div>)'

i = -1
if len(argv) > 1:
    i = int(argv[1])

txt = urllib.urlopen(URL+SEZIONE).read()
bar = re.findall(REGEX, txt.decode("windows-1252"))

if bar == []:
    print("Errore")
    exit(0)
if i == -1:
    i = int(random()*len(bar))
h = HTMLParser()
print(h.unescape(bar[i].replace("<br />", "\n")))
