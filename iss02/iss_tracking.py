#!/usr/bin/env python3
## Lab 41 - More APIs
##Written by Homer Walden

import urllib.request
import json
import turtle
import time

## Trace the ISS - earth-orbital space station
eoss = 'http://api.open-notify.org/iss-now.json'

## Call the webserv
trackiss = urllib.request.urlopen(eoss)

## put into file object
ztrack = trackiss.read()

## json 2 python data structure
result = json.loads(ztrack.decode('utf-8'))

## display our pythonic data
print("\n\nConverted python data")
print(result)
input('\nISS data retrieved & converted. Press any key to continue')    

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('\nLatitude: ', lat)
print('Longitude: ', lon)

## set screen size to 720x360
screen = turtle.Screen() # create a screen object
screen.setup(720, 360) # set the resolution

## set screen to match coordinates
screen.setworldcoordinates(-180,-90,180,90)

## adding map to the screen
screen.bgpic('iss_map.gif')

## register iss
screen.register_shape('spriteiss.gif')
iss = turtle.Turtle()
iss.shape('spriteiss.gif')
iss.setheading(90)

##move iss to correct location on the map
lon = round(float(lon))
lat = round(float(lat))

iss.penup()
iss.goto(lon, lat)
#turtle.mainloop()

yellowlat = 47.6
yellowlon = -122.3
mylocation = turtle.Turtle()
mylocation.penup()
mylocation.color('yellow')
mylocation.goto(yellowlon, yellowlat)
mylocation.dot(5)
mylocation.hideturtle()



#turtle.mainloop()

passiss = 'http://api.open-notify.org/iss-pass.json'
passiss = passiss + '?lat=' + str(yellowlat) + '&lon=' + str(yellowlon)
response = urllib.request.urlopen(passiss)
result = json.loads(response.read())
## print(result) ## uncomment to see the downloaded result

over = result['response'][1]['risetime']

style = ('Arial', 6, 'bold')
mylocation.write(time.ctime(over), font=style)