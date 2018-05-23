#!/usr/bin/env python3
#
#Written by Homer Walden

while(True):
   print('What is the L2 network protocol? ')
   hwprotocol=input()
   if hwprotocol=='eth':
      print('ethernet protocol allowed')
      break

   if hwprotocol=='fc':
      print('fiber channel NOT allowed')
      break

   if hwprotocol=='ifb':
      print('infiniband NOT allowed')
      break

   if hwprotocol=='otn':
      print('Optical Network allowed')
      break

   else:
      print('No idea what that technology is')
      break
      