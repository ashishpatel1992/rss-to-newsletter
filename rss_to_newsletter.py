from bs4 import BeautifulSoup
import requests
import io
import os.path
from os import path
import re
import feedparser
from job import Job

default_file = 'feed.xml'
default_url = 'http://emplois.truckstopquebec.com/feed/?post_type=noo_job'
default_encoding = 'utf-8'

# Check if sample XML file exist, if not then fetch from the internet
if not path.exists(default_file) or os.stat(default_file).st_size == 0:
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    })

    req = requests.get(default_url,headers)
    soup = BeautifulSoup(req.content,'html.parser')
    # print(soup.prettify())
    with io.open(file=default_file,mode='w',encoding=default_encoding) as write_file:
        write_file.writelines(soup.prettify())

print('LOG: Done fetching feed.xml!')
f = feedparser.parse(url_file_stream_or_string=default_file)

print(len(f['entries']))
# def key_at_depth(dict, depth):
#      if depth > 0:
#          return [ key for subdct in dict.itervalues() for key in key_at_depth(subdct, depth-1)  ]
#      else:
#          return dict.keys()
# # print(key_at_depth(f['entries'],1))

print(type(f['entries']))
for item in f['entries']:
    dictItem = dict(item)
    print(dictItem.keys())
    print(dictItem['title'])
    # print(dictItem)
    # print(len(dictItem.keys()))
#     job = Job(
#                 title=item['title'],
#                 title_detail=item['title_detail'],
#                 id=item['id'],
#                 summary=item['summary'],
#                 content=item['content'],
#                 company=item['company']
#             )
#     print(job.content[0].value)
#
#     # Templating using pythong for newsletter
