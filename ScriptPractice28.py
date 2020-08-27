#!/usr/bin/env python
import sys

def maxfunction(a,b,c):
    if (a > b) and (a > c):
        print('Max value is :',a)
    elif (b > a) and (b > c):
        print('Max value is :',b)
    elif (c > a) and (c > b):
        print('Max value is :',c)

if len(sys.argv) < 4:
    print('Usage <value1> <value2> <value3>')
    sys.exit ( 1 )

arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]

maxfunction(arg1,arg2,arg3)