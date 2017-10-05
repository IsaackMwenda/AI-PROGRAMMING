import urllib.request
import re

#connecting to strathmore URL
with urllib.request.urlopen('http://strathmore.edu/') as response:

#reading html code  and converting it from byte to string
   strathdata = response.read().decode('utf-8')

#Getting html links using re.findall    
   strathlinks = re.findall('"((http)s?://.*?)"', strathdata)
   for links in strathlinks:
       print(links)
