#!/usr/bin/env python

# Example 2: A Python program from the Raspberry Pi User Guide

username = raw_input("What is your name? ")

print "welcome to this calculator, ",username

goAgain = 1
while goAgain == 1:
	firstno = int(raw_input("Type the first number: "))
	secondno = int(raw_input("Type the second number: "))
	print firstno, "+", secondno, "=", firstno + secondno
	print firstno, "-", secondno, "=", firstno - secondno
	print firstno, "*", secondno, "=", firstno * secondno
	
	goAgain = int(raw_input("Type 1 to enter more numbers, or any other number to quit: "))
