import requests #for dowloading the web page
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

#dowloading web page
url='https://www.amazon.com/'
headers = {'Content-Type': 'text/html', 'Content-Length': '1203', 'Connection': 'keep-alive', 'Server': 'Server', 'Date': 'Sat, 12 Dec 2020 15:38:38 GMT', 'x-amz-rid': 'KEPTGB8ZE1VGGV62C608', 'Vary': 'Content-Type,Accept-Encoding,X-Amzn-CDN-Cache,X-Amzn-AX-Treatment,User-Agent', 'Last-Modified': 'Wed, 30 Sep 2020 23:54:00 GMT', 'ETag': '"a6f-5b0909d09d600-gzip"', 'Accept-Ranges': 'bytes', 'Content-Encoding': 'gzip', 'X-Cache': 'Error from cloudfront', 'Via': '1.1 5fa674fc9b94ee214ca1273ac912ec73.cloudfront.net (CloudFront)', 'X-Amz-Cf-Pop': 'MRS52-C1',
 'X-Amz-Cf-Id': 'cQQW0XbkcImCYRJmvu61zMFRRxk_PSoYV2KjnqJpLPM5IMnrvxKxcw=='}
response = requests.get(url,headers=headers)
print(response)