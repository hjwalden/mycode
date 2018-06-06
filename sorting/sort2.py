#!/usr/bin/env python3
##Written by Homer Walden
##Goal: create a function to be utilized as a key for sorting

##Create a list
firewall = [ 22, 80, 443, 25565, 5060, 5061, 123, 143 ]

##Create a funtion
def modTen(x): #modular math (remainder math)
    return x%10

##Print original list
print('\nOur list firewall looks like this:', firewall)

##Sort list using modTen fn as a key
print('\nOur list when we apply sorted(firewall, key=modTen):', sorted(firewall, key=modTen))

##Sort list using sort method and modTen as a key; permanently changes list
print('\nOur list when we apply list.sort():', firewall.sort(key=modTen))
print(firewall)