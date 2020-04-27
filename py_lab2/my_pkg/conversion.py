#!/usr/bin/python

#conversion

def conv():
	num = input("input binary number: ")
	num10 = int(num, 2)

	print("=> OCT> ",  format(num10, 'o'))
	print("=> DEC> ",  num10)
	print("=> HEX> ",  format(num10, 'X'))
