#!/usr/bin/env python3
#Demonstrating the utilization of APIs
#Written by Homer Walden

import urllib.request
import json
#Trace the ISS
majortom = 'http://api.open-notify.org/astros.json'

#Call the webservice
groundctrl = urllib.request.urlopen(majortom)

#Put fileobject into helmet
helmet = groundctrl.read()

#Decode json to python data structure
helmeston = json.loads(helmet.decode('utf-8')

#Display our pythonic data
print("Converted python data")
print(helmetson)

print(\n\n"People in Space: ", helmetson['number'])
people = helmetson['people']
print(people)