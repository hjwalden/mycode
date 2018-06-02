#!/usr/bin/env python3
#Create own script using while, if, elif, else statements
#Written by Homer Walden
            
while(True):
     answer=input('Hi, My name is_____?')
     if answer.lower()=='eminem' or answer.lower()=='shrubbery':
        print('You gave the super secret answer!')
        break             # break statement escapes the while loop
     else:
        print('Sorry, my name is Slim Shady!')