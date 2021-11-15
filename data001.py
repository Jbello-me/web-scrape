'''
change the url for each station
How to check if the url is downloadable?
'''
#!/usr/bin/env python3
# coding: utf-8
#import the following libraries
#region
import requests
import urllib.request
from urllib.request import urlopen
import urllib3
import time
from bs4 import BeautifulSoup # screen webscrapping
#endregion 


# import urllib2
import csv
import sys

url = 'https://wateroffice.ec.gc.ca/download/report_e.html?dt=dd&df=ddf&md=1&ext=csv'
response = urllib.request.urlopen(url)
html = response.read()

with open('output.csv', 'wb') as f:
        f.write(html)

'''
with requests.Session() as s:
    download = s.get(url)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        print(row)

'''
'''

url = 'https://wateroffice.ec.gc.ca/download/report_e.html?dt=dd&df=ddf&md=1&ext=csv'
urllib.request.urlretrieve(url, "001.csv")

downloaded_obj = requests.get(url)

with open("001.csv", "wb") as file:
    file.write(downloaded_obj.content)
'''

'''
url = 'https://wateroffice.ec.gc.ca/download/report_e.html?dt=dd&df=ddf&md=1&ext=csv'
r = requests.get(url, allow_redirects=True)
open("Nov.csv", 'wb').write(r.content)

csv_url ='https://wateroffice.ec.gc.ca/download/report_e.html?dt=dd&df=ddf&md=1&ext=csv'
print(csv_url)

req = requests.get(csv_url)
url_content = req.content
csv_file = open('downloaded.csv', 'wb')

csv_file.write(url_content)
csv_file.close()

'''

'''
#insert the url for the data
url = 'https://wateroffice.ec.gc.ca/download/report_e.html?dt=dd&df=ddf&md=1&ext=csv'
#connect to the url
response = requests.get(url)
print (response) # <Response [200]> means that access was successful 

#parse the html code with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")
all = soup.findAll('a')
print("\n")
print(all)

#Miss. Code
#region
# r = requests.get(url, allow_redirects=True)
# print(r.headers.get('content-type'))
#endregion

'''
