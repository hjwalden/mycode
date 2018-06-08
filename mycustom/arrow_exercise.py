#!/usr/bin/env python3

python3 -m pip install arrow
import arrow

utc = arrow.utcnow()
print('\narrow.utcnow is ', utc)

utc = utc.shift(hours=-1)
print('\nutc.shift is ', utc)

local = utc.to('US/Pacific')
print('\nutc.to is ', local)

local.timestamp
print('\nlocal.timestamp is ', str(local.timestamp))

local.humanize()
print('\nlocal.humanize is ', str(local.humanize()))

whattime = arrow.get(1528408131)
print('\narrow.get is ', whattime)

zach = "Zach was born on April 30 1984 in the year of our lord and savior"
x = arrow.get(zach, 'MMMM DD YYYY')
print('\n', zach, x)

x.timestamp

y = arrow.get(logfile, 'YYYY-MM-DDTHH:mm:ss')
