import os
import pygame
pygame.init();

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Flappy Bird Adaptation')
pygame.display.update()		#only updates portion specified

gameExit = False
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True


#required
pygame.quit()
quit()	