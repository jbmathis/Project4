import os
import pygame
pygame.init();

#colors
white = (255,255,255)
#position vars
background_x = 0
background_y = 0
mich_x = 50
mich_y = 100

class Michigan(pygame.sprite.Sprite):
        WIDTH = 50
        HEIGHT = 50
        SINK_SPEED = 0.18
        CLIMB_SPEED = 0.3
        CLIMB_DURATION = 333.3

        def __init__(self, x, y, msec_to_climb, image):
                super(Michigan, self).__init__()
                self.x = mich_x
                self.y = mich_y
                self.image = image
                
def load_images():
        def load_image(image_name):
                 img = pygame.image.load(os.path.join('images', image_name))
                 return img
        return {'Michigan_Wolverines_Field': load_image('Michigan_Wolverines_Field.bmp'),
                'block_m': load_image('block_m.bmp')}


def main():
        gameDisplay = pygame.display.set_mode((950,475))
        pygame.display.set_caption('Jessica Game')
        gameDisplay.fill(white)
        pygame.display.update()		#only updates portion specified
        #create the dictionary of photos
        images = load_images()
        background = images['Michigan_Wolverines_Field']
        player = Michigan(mich_x, mich_y, 2, images['block_m'])

        gameExit = False
        while not gameExit:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                gameExit = True
                gameDisplay.blit(images['Michigan_Wolverines_Field'], (background_x, background_y))
                gameDisplay.blit(images['block_m'], (mich_x, mich_y))
                pygame.display.update()
	
main()

#required
pygame.quit()
quit()	
