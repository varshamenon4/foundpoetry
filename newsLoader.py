#!/usr/bin/env python3
import requests

api_key = "7a6eb10b9fe649d89880147964ba83ca"
topic = 'Black Lives Matter'

url = ('http://newsapi.org/v2/everything?'
       'q=' + topic + '&'
       'from=2020-09-03&'
       'sortBy=popularity&'
       'apiKey=' + api_key)

response = requests.get(url)

print(response.json())

