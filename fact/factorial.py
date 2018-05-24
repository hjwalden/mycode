#!/usr/bin/env python3
#Scripting using for loops and range()
#Written by Homer Walden

x=int(input("Enter a number: "))
f=1

#Change here was to make x into x+1
for i in range(1, x+1):
   f=f * i
print(str(x) + '! = ' + str(f))