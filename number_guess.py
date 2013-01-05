#!/usr/bin/env python

import wiringPy
import random
import time
import pygame

def play_sound(filename, delay=0):
	pygame.mixer.music.load(filename)
	pygame.mixer.music.play()
	time.sleep(delay)

random.seed()
pygame.init()

wiringPy.setup()
for pin in range(0,8):
	wiringPy.pin_mode(pin, 1)
	
wiringPy.digital_write_byte(255)

play_sound("sounds/yodel.mp3")
name = raw_input("What is your name? ")

print "hello " + name

levels = { 'easy': 10, 'medium': 100, 'hard': 500 }
game_type = raw_input("choose level: easy, medium or hard? ")
max_number = levels[game_type]
answer = random.randint(1, max_number)
lights = [0,1,3,7,15,31,63,127,255]
lives = 8

print "guess which number I am thinking of [between 1 and " + str(max_number) + "]"

while (True):
	guess = int(raw_input("> "))

	if guess == answer:
		print "correct, you win!"
		play_sound("sounds/ding.mp3", 2)
		play_sound("sounds/applause.mp3", 3)
		exit()

	lives -= 1
	play_sound("sounds/buzzer.mp3", 1)
	wiringPy.digital_write_byte(lights[lives])
	
	if lives == 0:
		print "game over, you lose - i was thinking of " + str(answer) + " !"
		play_sound("sounds/trombone.mp3", 4)
		exit()
	
	if guess < answer:
		print "wrong, go higher!!"
	else:
		print "wrong, go lower!!"

	print "try again"
