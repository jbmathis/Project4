import os
import pygame
import random
import sys
pygame.init();

#colors
white = (255,255,255)
#window size
X_MAX = 950
Y_MAX = 475
#position vars
background_x = 0
background_y = 0
mich_x = 75
mich_y = 100
block_init_x = 800
block_init_y_top = 0
block_init_y_bottom = 375

everything = pygame.sprite.Group()

class Michigan(pygame.sprite.Sprite):

        def __init__(self, x, y, image):
                super(Michigan, self).__init__()
                self.image = image
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.rect.height = 10
                self.rect.width = 10
                self.add(everything)

        def rect(self):
                return self.image.get_rect()
       
        def update(self):
                self.rect.y += 5
                self.rect.x += 1

class Block(pygame.sprite.Sprite):
        
        def __init__(self, x, y, image):
                super(Block, self).__init__()
                self.image = image
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.add(everything)
                
        def rect(self):
                return self.image.get_rect()
        
        def update(self):
                self.rect.x -= 10
                if self.rect.x < 0:
                        self.rect.x = random.randint(300,950)

class Enemy(pygame.sprite.Sprite):
        def __init__(self, x, y, image):
                super(Enemy,self).__init__()
                self.image = image
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect. y = y
                self.add(everything)

        def rect(self):
                return self.image.get_rect()

        def update(self):
                self.rect.x -= 10
                if self.rect.x < 0:
                        self.rect.x = random.randint(300,950)
                              
def load_images():
        def load_image(image_name):
                 img = pygame.image.load(os.path.join('images', image_name))
                 return img.convert_alpha()
        return {'Michigan_Wolverines_Field': load_image('Michigan_Wolverines_Field.bmp'),
                'block_m': load_image('block_m.bmp'), 'block': load_image('block.bmp')}


def main():
        gameDisplay = pygame.display.set_mode((X_MAX, Y_MAX))
        pygame.display.set_caption('B1G Flappy Bird')
        gameDisplay.fill(white)
        pygame.display.update()
        empty = pygame.Surface((X_MAX, Y_MAX))
        
        #create the dictionary of photos
        images = load_images()
        background = images['Michigan_Wolverines_Field']

        #create the player and the blocks
        player = Michigan(mich_x, mich_y, images['block_m'])
        for i in range(5):
            pos_init = random.randint(300, 950)
            Block(pos_init, block_init_y_top, images['block'])
            Block(pos_init, block_init_y_bottom, images['block'])

        health_font = pygame.font.SysFont(None, 32, bold=True)
        health = 100
        health_surface = health_font.render('Health: ' + str(health), True, (0, 0, 0))
        gameDisplay.blit(health_surface, (100, 450))
        
        gameExit = False
        Lose = False
        while not gameExit:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                gameExit = True
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_UP:
                                        player.rect.y -= 75

                if player.rect.y == 475 or player.rect.y == 0:
                        Lose = True

                if Lose == True:
                        pass                       

                everything.clear(gameDisplay, empty)
                everything.update()
                everything.draw(gameDisplay)
                pygame.display.flip()

                gameDisplay.blit(images['Michigan_Wolverines_Field'], (background_x, background_y))
                gameDisplay.blit(images['block_m'], player.rect)
                #gameDisplay.blit(images['block'], everything.Block.rect)
                # gameDisplay.blit(images['block'], block_bottom.rect)
                gameDisplay.blit(health_surface, (100, 450))
        
main()

#required
pygame.quit()
quit()	
