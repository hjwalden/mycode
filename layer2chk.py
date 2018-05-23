#!/usr/bin/env python3
#Using while, if, elif, and else statement 
#Written by Homer Walden

while(True):
   print('What is the L2 network protocol? ')
   hwprotocol=input()
   if hwprotocol=='eth':
      print('ethernet protocol allowed')
      break

   elif hwprotocol=='fc':
      print('fiber channel NOT allowed')
      break

   elif hwprotocol=='ifb':
      print('infiniband NOT allowed')
      break

   elif hwprotocol=='otn':
      print('Optical Network allowed')
      break

   else:
      print('No idea what that technology is')
      break
      