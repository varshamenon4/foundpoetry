#!/usr/bin/env python3
import requests

# Get most popular article based on topic
api_key = "7a6eb10b9fe649d89880147964ba83ca"
topic = 'Black Lives Matter'
# Add date

url = ('http://newsapi.org/v2/everything?'
       'q=' + topic + '&'
       'from=2020-09-03&'
       'sortBy=popularity&'
       'language=en&'
       'apiKey=' + api_key)

response = requests.get(url)

r_json = response.json()

print(r_json['articles'][0]['title'])
print(r_json['articles'][0]['url'])

# Get full contents of article

