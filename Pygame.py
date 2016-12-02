import os
import pygame
import pygame.mixer
import random
import sys

#required
pygame.init();

#colors
white = (255,255,255)
#window size
X_MAX = 950
Y_MAX = 472
#position vars
background_x = 0
background_y = 0
mich_x = 75
mich_y = 100
block_init_y_top = 0
block_init_y_bottom = 375
ref_init_y_bottom = 300
win_screen_x = 53
lose_screen_x = 130

#sprite groups for all objects and all enemies
everything = pygame.sprite.Group()
enemies = pygame.sprite.Group()

#main player, automatically falls and progresses across screen
class Michigan(pygame.sprite.Sprite):

        def __init__(self, x, y, image):
                super(Michigan, self).__init__()
                self.image = image
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.health = 100
                self.add(everything)

        def rect(self):
                return self.image.get_rect()
       
        def update(self):
                self.rect.y += 5
                self.rect.x += 1

        def reduce_health(self):
                self.health -= 5

#obstacles, automatically progress toward player
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
                        
#obstacle inherited from Block, moves faster
class Referee(Block):
        
        def __init__(self, x, y, image):
                Block.__init__(self, x, y, image)

        def update(self):
                self.rect.x -= 10
                if self.rect.x < 0:
                        self.rect.x = random.randint(300,950)
                
#load images needed for the game                              
def load_images():
        def load_image(image_name):
                 img = pygame.image.load(os.path.join('images', image_name))
                 img = img.convert_alpha()
                 return img
        return {'Michigan_Wolverines_Field': load_image('Michigan_Wolverines_Field.bmp'),
                'Harbaugh': load_image('Harbaugh.png'), 'block': load_image('block.bmp'),
                'Game_Over': load_image('Game_Over.bmp'), 'ref_top': load_image('ref_top.png'),
                'ref_bottom': load_image('ref_bottom.png'), 'Win_Screen': load_image('Win_Screen.png')}

#main play game function
def main():
        #create the window and caption
        gameDisplay = pygame.display.set_mode((X_MAX, Y_MAX))
        pygame.display.set_caption('B1G Flappy Bird')
        gameDisplay.fill(white)
        pygame.display.update()
        
        #create the dictionary of photos
        images = load_images()

        #create the player and the blocks, randomizing start x for blocks
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
                
        #display health score on screen
        health_font = pygame.font.SysFont(None, 32, bold=True)
        health_surface = health_font.render('Health: ' + str(player.health), True, (0, 0, 0))
        gameDisplay.blit(health_surface, (100, 450))

        #boolean vars for game loop, losing, and winning
        gameExit = False
        Lose = False
        Win = False

        #load sounds and play background music
        background_sound = pygame.mixer.Sound('stadium_sound.wav')        
        background_sound.play()
        collision_sound = pygame.mixer.Sound('referee.wav')

        #game play loop
        while not gameExit:
                #check for quit and up arrow action from user
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                gameExit = True
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_UP:
                                        player.rect.y -= 75
                                        
                #collision detection, play sound and reduce health
                for enemy in enemies:
                        if pygame.sprite.collide_rect(player, enemy):
                                player.reduce_health()
                                collision_sound.play()
                                health_surface = health_font.render('Health: ' + str(player.health), True, (0, 0, 0))
                                gameDisplay.blit(health_surface, (100, 450)) 

                #if player's health runs out or goes off screen, lose game
                if player.health <= 0:
                        Lose = True
                if player.rect.y == 475 or player.rect.y == 0:
                        Lose = True
                #if player makes it to the endzone
                if player.rect.x == 760:
                        Win = True
                        
                #if player loses the game
                if Lose == True:
                        #kill objects on screen
                        for sprite in everything.sprites():
                                sprite.kill()
                        #load background image and text to display
                        gameDisplay.fill(white)
                        gameDisplay.blit(images['Game_Over'], (lose_screen_x, background_y))
                        font = pygame.font.SysFont('times new roman', 32)
                        score_font = pygame.font.SysFont('times new roman', 40, True)
                        over_surface = font.render('\"I\'m bitterly disappointed', True, white)
                        gameDisplay.blit(over_surface, (490, 100))
                        over_surface = font.render('with the officiating', True, white)
                        gameDisplay.blit(over_surface, (515, 140))
                        over_surface = font.render('of this game.\"', True, white)
                        gameDisplay.blit(over_surface, (530, 180))
                        over_surface = score_font.render('Try again!', True, white)
                        gameDisplay.blit(over_surface, (590, 220))
                        pygame.display.update()
                        exit()
                        
                #if player wins the game
                if Win == True:
                        #kill objects on screen
                        for sprite in everything.sprites():
                                sprite.kill()
                        #load background image and text to display
                        gameDisplay.fill(white)
                        gameDisplay.blit(images['Win_Screen'], (win_screen_x, background_y))
                        font = pygame.font.SysFont('times new roman', 32)
                        score_font = pygame.font.SysFont('times new roman', 40, True)
                        over_surface = font.render('You attacked this game', True, white)
                        gameDisplay.blit(over_surface, (80, 100))
                        over_surface = font.render('with an enthusiasm', True, white)
                        gameDisplay.blit(over_surface, (80, 150))
                        over_surface = font.render('unknown to mankind!', True, white)
                        gameDisplay.blit(over_surface, (80, 200))
                        over_surface = score_font.render('Score: ' + str(player.health), True, white)
                        gameDisplay.blit(over_surface, (115, 250))
                        pygame.display.update()
                        exit()                      
                
                #update the screen and images
                everything.update()
                everything.draw(gameDisplay)
                pygame.display.flip()
                gameDisplay.blit(images['Michigan_Wolverines_Field'], (background_x, background_y))
                gameDisplay.blit(images['Harbaugh'], player.rect)
                gameDisplay.blit(health_surface, (100, 450))
                
#run the game        
main()

#required
pygame.quit()
quit()	
