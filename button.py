#!/usr/bin/env python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
while True:
    input_value = GPIO.input(18)
    if input_value == False:
        print("The button was pressed")
        while (input_value == False):
            input_value = GPIO.input(18)

