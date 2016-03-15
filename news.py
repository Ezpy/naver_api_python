# -*- coding: utf-8 -*-

import urllib2

client_id = 'your-client-id'
client_secret = 'your-client-secret'
search_word = 'your-search-word'

url = 'https://openapi.naver.com/v1/search/news.xml?query=%s' % search_word

request = urllib2.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib2.urlopen(request)
response_body = response.read()

print response_body.decode('utf-8')
