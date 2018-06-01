#!/usr/bin/env python

a = " !\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^abcdefghijklmnopqrstuvwxyz"
ans =""
flag = [233, 129, 9, 5, 130, 194, 195, 39, 75, 229]
for char in a:
    x = (((ord(char) << 5) | (ord(char) >> 3)) ^ 111) & 255
    if x in flag:
    	ans += char

print ans

password = "4w3SomeB!T"