#!/usr/bin/env python3

def OnlyCharNum(st):
    return(''.join([x for x in st if isChar(x) or isNum(x)]))

def isChar(x):
    return((x>='a' and x<='z') or (x>='A' and x<='Z'))

def isNum(x):
    return(x>='0' and x<='9')

s = input("Input:")
print("Output:", OnlyCharNum(s))
