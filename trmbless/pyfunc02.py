#!/usr/bin/env python3
#Defining Functions and formating text
#Written by Homer Walden

from blessings import Terminal
t = Terminal()
print(t.clear())
print(t.bold_black_on_yellow('Print yellow text'))

def yellow_np():
   print(t.bold_black_on_yellow('Print yellow text'))

def yellow_wp(p):
   print(t.bold_black_on_yellow(p))

yellow_np()

yellow_wp("I want this to print in YELLOW")