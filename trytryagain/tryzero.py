#!/usr/bin/env python3
##Lab 40 - Try and Except 02
##Written by Homer Walden

try:                                                           ##code we want to try to run goes under the try
    print('Enter a numerator: ')
    numerator = int(input())                                   ##numerator as input
    raise KeyError                                             ##raise Key Error
    print('Enter a denominator: ')
    denominator = int(input())                                 ##denominator as input
    print(numerator / denominator)                             ##write remainder of division of equation
except ZeroDivisionError:                                      ##only catches div by zero errors
    print('**Not a legal entry**\nEnter a numerator: ')
    numerator = int(input())
    print('Enter a denominator: ')
    denominator = int(input())
    print(numerator / denominator)
except KeyError:                                               ##exception for raised argument
    print('End of File Error')
except:
    print("We're sorry, something unexpected happened. See your IT department.")