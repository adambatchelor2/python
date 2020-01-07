
#https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

import requests

url = 'http://github.com'
r = requests.get(url)
r_html = r.text

print (r_html)