#!/usr/bin/env python

import wiringPy
import time

wiringPy.setup()
for pin in range(0,8):
	wiringPy.pin_mode(pin, 1)

wiringPy.digital_write_byte(255)

print "whats your name?"
name = raw_input()

print "hello " + name

doubles = [1,2,4,8,16,32,64,128]
snooze = 0.1

while (True):
	for no in doubles:
		wiringPy.digital_write_byte(no) 
		time.sleep(snooze)
	
	doubles.reverse()

#for no in range (0,256):
#	wiringPy.digital_write_byte(no) 
#	time.sleep(0.0625)

