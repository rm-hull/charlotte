#!/usr/bin/env python

# Snake game

import pygame, sys, time, random
from  pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
playSurface = pygame.display.set_mode((640,480))
pygame.display.set_caption('Raspberry Snake')

redColor = pygame.Color(255,0,0)
blackColor = pygame.Color(0,0,0)
whiteColor = pygame.Color(255,255,255)
greyColor = pygame.Color(150,150,150)

snakePosition = [100,100]
snakeSegments = [[100,100],[80,100],[60,100]]
raspberryPosition = [300,300]
raspberrySpawned = 1
direction = 'right'
changeDirection = direction

def gameOver():
	gameOverFont = pygame.font.Font('freesansbold.ttf',72)
	gameOverSurf = gameOverFont.render('Game Over', True, greyColor)
	gameOverRect = gameOverSurf.get_rect()
	gameOverRect.midtop = (320, 10)
	playSurface.blit(gameOverSurf, gameOverRect)
	pygame.display.flip()
	time.sleep(5)
	pygame.quit()
	sys.exit()
	
gameOver()
