import os
import pygame
pygame.init();

#colors
white = (255,255,255)
#position vars
background_x = 0
background_y = 0
mich_x = 75
mich_y = 225
block_init_x = 600
block_init_y_top = 50
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

class Block(pygame.sprite.Sprite):
        
        def __init__(self, x, y, image):
                self.image = image
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
        def rect(self):
                return self.image.get_rect()
                
                
                
def load_images():
        def load_image(image_name):
                 img = pygame.image.load(os.path.join('images', image_name))
                 return img
        return {'Michigan_Wolverines_Field': load_image('Michigan_Wolverines_Field.bmp'),
                'block_m': load_image('block_m.bmp'), 'block': load_image('block.bmp')}


def main():
        gameDisplay = pygame.display.set_mode((950,475))
        pygame.display.set_caption('Jessica Game')
        gameDisplay.fill(white)
        pygame.display.update() #only updates portion specified
        
        #create the dictionary of photos
        images = load_images()
        background = images['Michigan_Wolverines_Field']
        player = Michigan(mich_x, mich_y, 2, images['block_m'])

        clock = pygame.time.Clock()
        time_elapsed = 0
        
        gameExit = False
        while not gameExit:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                gameExit = True
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                                player.rect.y -= 10

                time = clock.tick()
                time_elapsed += time
                if time_elapsed % 5 == 0:
                        player.rect.y += 20
                        

                if time_elapsed % 25 == 0:
                        block_top = Block(block_init_x, block_init_y_top, images['block'])
                        block_bottom = Block(block_init_x, block_init_y_bottom, images['block'])
                        gameDisplay.blit(images['block'], block_top.rect)
                        gameDisplay.blit(images['block'], block_bottom.rect)
                        pygame.display.update()

                if player.rect.y == 475:
                        gameExit == True

                gameDisplay.blit(images['Michigan_Wolverines_Field'], (background_x, background_y))
                gameDisplay.blit(images['block_m'], player.rect)
                pygame.display.update()
                player.update()
	
main()

#required
pygame.quit()
quit()	
