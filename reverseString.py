from array import *

def rev(strng):
    if len(strng) <= 1:
        return strng
    return strng[len(strng)-1] + rev(strng[0:len(strng)-1])

print(rev('python'))