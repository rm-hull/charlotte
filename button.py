#!/usr/bin/env python

# Button tester program: supply the BCM GPIO port as the first arg

import RPi.GPIO as GPIO
import sys

port = int(sys.argv[1])

GPIO.setmode(GPIO.BCM)
GPIO.setup(port, GPIO.IN)
while True:
    input_value = GPIO.input(port)
    if input_value == False:
        print("The button was pressed")
        while (input_value == False):
            input_value = GPIO.input(port)

