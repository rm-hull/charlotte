#!/usr/bin/env python

# Snake game

import pygame, sys, time, random
from  pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
playSurface = pygame.display.set_mode((640,480))
pygame.display.set_caption('Raspberry Snake')

redColor = pygame.Color(255,0,0)
greenColor = pygame.Color(0,255,0)
blackColor = pygame.Color(0,0,0)
whiteColor = pygame.Color(255,255,255)
greyColor = pygame.Color(150,150,150)

snakePosition = [100,100]
snakeSegments = [[100,100],[80,100],[60,100]]
raspberryPosition = [300,300]
raspberrySpawned = 1
direction = 'right'
changeDirection = direction
score = 0

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
	
def displayScore(score):
	scoreFont = pygame.font.Font('freesansbold.ttf',16)
	scoreSurf = scoreFont.render('score: ' + str(score), True, greenColor)
	scoreRect = scoreSurf.get_rect()
	scoreRect.midtop = (320, 10)
	playSurface.blit(scoreSurf, scoreRect)
	
while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_RIGHT :
				changeDirection = 'right'
			if event.key == K_LEFT :
				changeDirection = 'left'
			if event.key == K_UP :
				changeDirection = 'up'
			if event.key == K_DOWN :
				changeDirection = 'down'
			if event.key == K_ESCAPE:
				pygame.event.post(pygame.event.Event(QUIT))
				
	if changeDirection == 'right' and not direction == 'left':
		direction = changeDirection
	if changeDirection == 'left' and not direction == 'right':
		direction = changeDirection	
	if changeDirection == 'up' and not direction == 'down':
		direction = changeDirection	
	if changeDirection == 'down' and not direction == 'up':
		direction = changeDirection	
	
	if direction == 'right':
		snakePosition[0] += 20	
	if direction == 'left':
		snakePosition[0] -= 20
	if direction == 'up':
		snakePosition[1] -= 20
	if direction == 'down':
		snakePosition[1] += 20
		
	snakeSegments.insert(0,list(snakePosition))
	
	if snakePosition[0] == raspberryPosition[0]	and snakePosition[1] == raspberryPosition[1]:
		raspberrySpawned = 0
		score += 1
	else:
		snakeSegments.pop()	
		
	if raspberrySpawned == 0:
		x = random.randrange(1,32)
		y = random.randrange(1,24)
		raspberryPosition = [int(x*20),int(y*20)]
	raspberrySpawned = 1	
	
	playSurface.fill(blackColor)
	displayScore(score)
	for position in snakeSegments:
		pygame.draw.rect(playSurface,whiteColor,Rect(position[0],position[1],20,20)) 
		pygame.draw.rect(playSurface,redColor,Rect(raspberryPosition[0],raspberryPosition[1],20,20))
	pygame.display.flip()
	
	if snakePosition[0] > 620 or snakePosition[0] < 0:
		gameOver()
	if snakePosition[1] > 460 or snakePosition[1] < 0:
		gameOver()	
	for snakeBody in snakeSegments[1:]:
		if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
			gameOver()
			
	fpsClock.tick(20)
