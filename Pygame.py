import os
import pygame
from collections import deque
pygame.init();

#colors
white = (255,255,255)
#position vars
background_x = 0
background_y = 0
mich_x = 75
mich_y = 100
block_init_x = 800
block_init_y_top = 0
block_init_y_bottom = 375

class Michigan(pygame.sprite.Sprite):

        def __init__(self, x, y, msec_to_climb, image):
                super(Michigan, self).__init__()
                self.image = image
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.rect.height = 10
                self.rect.width = 10

        def rect(self):
                return self.image.get_rect()
       
        def update(self):
                self.rect.y += 2
                self.rect.x += 1

class Block(pygame.sprite.Sprite):
        
        def __init__(self, x, y, image):
                self.image = image
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                
        def rect(self):
                return self.image.get_rect()
        
        def update(self):
                self.rect.x -= 15
                
                
                
def load_images():
        def load_image(image_name):
                 img = pygame.image.load(os.path.join('images', image_name))
                 return img
        return {'Michigan_Wolverines_Field': load_image('Michigan_Wolverines_Field.bmp'),
                'block_m': load_image('block_m.bmp'), 'block': load_image('block.bmp')}


def main():
        gameDisplay = pygame.display.set_mode((950,475))
        pygame.display.set_caption('B1G Flappy Bird')
        gameDisplay.fill(white)
        pygame.display.update() #only updates portion specified
        
        #create the dictionary of photos
        images = load_images()
        background = images['Michigan_Wolverines_Field']
        player = Michigan(mich_x, mich_y, 2, images['block_m'])
        block_top = Block(block_init_x, block_init_y_top, images['block'])
        block_bottom = Block(block_init_x, block_init_y_bottom, images['block'])
        

        BLOCKS_EVENT = pygame.USEREVENT + 1
        i = 1
        
        clock = pygame.time.Clock()
        time_elapsed = 0

        pygame.time.set_timer(BLOCKS_EVENT, 250)
        
        blocks = list()
        blocks.append(block_top)
        blocks.append(block_bottom)

        score_font = pygame.font.SysFont(None, 32, bold=True)
        health = 100
        health_surface = health_font.render('Health: ' + str(health), True, (0, 0, 0))
        gameDisplay.blit(health_surface, (100, 450))
        
        gameExit = False
        while not gameExit:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                gameExit = True
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_UP:
                                        player.rect.y -= 25
                        if event.type == BLOCKS_EVENT:
                                for block in blocks:
                                        block.update()
                                        gameDisplay.blit(images['block'], block.rect)
                                        pygame.display.update()
                                        if block.rect.x < 5:
                                                blocks.remove(block)
                                        if i == 30:
                                                blocks.append(Block(block_init_x, block_init_y_top, images['block']))
                                                blocks.append(Block(block_init_x , block_init_y_bottom, images['block']))
                                                i = 0
                                i += 1

                time = clock.tick()
                time_elapsed += time
                if time_elapsed % 5 == 0:
                        player.update()
                        pygame.display.update()

                if player.rect.y == 475:
                        gameExit == True

                player.update()
                pygame.display.update()
                gameDisplay.blit(images['Michigan_Wolverines_Field'], (background_x, background_y))
                gameDisplay.blit(images['block_m'], player.rect)
                gameDisplay.blit(images['block'], block_top.rect)
                gameDisplay.blit(images['block'], block_bottom.rect)
                gameDisplay.blit(health_surface, (100, 450))
        pygame.display.update()
        
	
main()
#required
pygame.quit()
quit()	
