#!/usr/bin/env python3
#Lab 39 - Try and Except Part 01
#Written by Homer Walden

try:
    print('Enter a file name: ')
    name = input()
    file = open(name, 'w')
except:
    print('Error with that file name!')
    print('Enter a file name: ')
    name = input()
    file = open(name, 'w')
finally:
    print('This code will always execute')