#!/usr/bin/env python3
import requests
from datetime import date

# Get most popular article based on topic
api_key = "7a6eb10b9fe649d89880147964ba83ca"
topic = 'Black Lives Matter'
# Add date
today = str(date.today())
print(str(today))

url = ('http://newsapi.org/v2/everything?'
       'q=' + topic + '&'
       'from=' + today + '&'
       'sortBy=popularity&'
       'language=en&'
       'apiKey=' + api_key)

response = requests.get(url)

r_json = response.json()

print(r_json['articles'][0]['title'])
print(r_json['articles'][0]['url'])

# Get full contents of article
rtcl_url = r_json['articles'][0]['url']

rtcl_r = requests.get(rtcl_url)

#print(rtcl_r.text)