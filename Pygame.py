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
ref_init_y_bottom = 300

everything = pygame.sprite.Group()
enemies = pygame.sprite.Group()
user = pygame.sprite.Group()

class Michigan(pygame.sprite.Sprite):

        def __init__(self, x, y, image):
                super(Michigan, self).__init__()
                self.image = image
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.rect.height = 10
                self.rect.width = 10
                self.health = 100
                self.add(everything)
                self.add(user)

        def rect(self):
                return self.image.get_rect()
       
        def update(self):
                self.rect.y += 5
                self.rect.x += 1

        def reduce_health(self):
                self.health -= 5

class Block(pygame.sprite.Sprite):
        
        def __init__(self, x, y, image):
                super(Block, self).__init__()
                self.image = image
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.add(everything)
                self.add(enemies)
                
        def rect(self):
                return self.image.get_rect()
        
        def update(self):
                self.rect.x -= 5
                if self.rect.x < 0:
                        self.rect.x = random.randint(300,950)

class Referee(Block):
        
        def __init__(self, x, y, image):
                Block.__init__(self, x, y, image)

        def update(self):
                self.rect.x -= 10
                if self.rect.x < 0:
                        self.rect.x = random.randint(300,950)
                              
def load_images():
        def load_image(image_name):
                 img = pygame.image.load(os.path.join('images', image_name))
                 img = img.convert_alpha()
                 return img
        return {'Michigan_Wolverines_Field': load_image('Michigan_Wolverines_Field.bmp'),
                'Harbaugh': load_image('Harbaugh.png'), 'block': load_image('block.bmp'),
                'Game_Over': load_image('Game_Over.bmp'), 'ref_top': load_image('ref_top.png'),
                'ref_bottom': load_image('ref_bottom.png'), 'Win_Screen': load_image('Win_Screen.png')}


def main():
        gameDisplay = pygame.display.set_mode((X_MAX, Y_MAX))
        pygame.display.set_caption('B1G Flappy Bird')
        gameDisplay.fill(white)
        pygame.display.update()
        empty = pygame.Surface((X_MAX, Y_MAX))
        
        #create the dictionary of photos
        images = load_images()

        #create the player and the blocks
        player = Michigan(mich_x, mich_y, images['Harbaugh'])
        for i in range(3):
                pos_init = random.randint(300, 950)
                Block(pos_init, block_init_y_top, images['block'])
                Block(pos_init, block_init_y_bottom, images['block'])
        for i in range(2):
                pos_init_1 = random.randint(400, 950)
                pos_init_2 = random.randint(400, 950)
                Referee(pos_init_1, block_init_y_top, images['ref_top'])
                Referee(pos_init_2, ref_init_y_bottom, images['ref_bottom'])
                

        health_font = pygame.font.SysFont(None, 32, bold=True)
        health_surface = health_font.render('Health: ' + str(player.health), True, (0, 0, 0))
        gameDisplay.blit(health_surface, (100, 450))
        
        gameExit = False
        Lose = False
        Win = False
        while not gameExit:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                gameExit = True
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_UP:
                                        player.rect.y -= 75

                for enemy in enemies:
                        if player.rect.colliderect(enemy.rect):
                                player.reduce_health()
                                health_surface = health_font.render('Health: ' + str(player.health), True, (0, 0, 0))
                                gameDisplay.blit(health_surface, (100, 450)) 

                #hit_enemy = pygame.sprite.groupcollide(user, enemies, False, False)
                #for k,v in hit_enemy.items():
                        #print(v)
                        #k.reduce_health()
                        #print(k.health)
                        #health_surface = health_font.render('Health: ' + str(k.health), True, (0, 0, 0))
                        #gameDisplay.blit(health_surface, (100, 450))
                        

                if player.rect.y == 475 or player.rect.y == 0:
                        Lose = True

                if player.rect.x == 760:
                        Win = True

                if Lose == True:
                        for sprite in everything.sprites():
                                sprite.kill()
                        gameDisplay.fill(white)
                        gameDisplay.blit(images['Game_Over'], (background_x, background_y))
                        pygame.display.update()
                        gameExit = True

                if Win == True:
                        for sprite in everything.sprites():
                                sprite.kill()
                                gameDisplay.fill(white)
                                gameDisplay.blit(images['Win_Screen'], (background_x, background_y))
                                pygame.display.update()
                                gameExit = True                       
                        

                everything.update()
                everything.draw(gameDisplay)
                pygame.display.flip()

                gameDisplay.blit(images['Michigan_Wolverines_Field'], (background_x, background_y))
                gameDisplay.blit(images['Harbaugh'], player.rect)
                gameDisplay.blit(health_surface, (100, 450))
        
main()

#required
pygame.quit()
quit()	
