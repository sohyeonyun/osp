#!/usr/bin/python
import my_pkg

while True:
	menu = int(input("Select menu: 1)conversion 2)union/intersection 3)exit? "))
	
	if (menu == 1):
		my_pkg.conv()
	elif (menu == 2):
		my_pkg.operation()
	elif (menu == 3):
		print("Exit the program...")
		break
	else:
	 	print("Wrong menu!")

