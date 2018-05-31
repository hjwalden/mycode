#!/usr/bin/env python3
##Lab 40 - Try and Except 02 - Part 2
##Written by Homer Walden

try:                                                                      ##code we want to try to run goes under the try
    print("This is what we try to do, but we can raise an error...")
    raise IOError                                                         ##raise an error
except ZeroDivisionError:                                                 ##only catches div by zero errors
    print("Computers do not like div by zero")
except IOError:
    print("This code raised an IO error")
except:
    print("We're sorry, something unexpected happened. See your IT department.")