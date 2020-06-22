import sys
import time
import random
import pygame
from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)
IMAGEWIDTH = 300
IMAGEHEIGHT = 200
FPS = 60

class Mosquito(pygame.sprite.Sprite):
    def __init__(self, width, height, random_x, random_y, window_width, window_height):
        super().__init__()
        #load the picture
        self.raw_image = pygame.image.load('./mosquito.png').convert_alpha()#change the pixel format of an image including per pixel alphas(rtype Surface)
        # make the picture smaller 
        self.image = pygame.transform.scale(self.raw_image, (width, height))
        # return the position
        self.rect = self.image.get_rect()
        #locate
        self.rect.topleft = (random_x, random_y)
        self.width = width
        self.height = height
        self.window_width = window_width
        self.window_height = window_height

def get_random_position(window_width, window_height, image_width, image_height):
    random_x = random.randint(image_width, window_width - image_width)
    random_y = random.randint(image_height, window_height - image_height)
    return random_x, random_y

def main():
    pygame.init()

    #load window surface
    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Mosquito War')
    random_x, random_y = get_random_position(WINDOW_WIDTH, WINDOW_HEIGHT, IMAGEWIDTH, IMAGEHEIGHT)
    mosquito = Mosquito(IMAGEWIDTH, IMAGEHEIGHT, random_x, random_y, WINDOW_WIDTH, WINDOW_HEIGHT)
    reload_mosquito_event = USEREVENT + 1
    pygame.time.set_timer(reload_mosquito_event, 300)
    points = 0
    my_font = pygame.font.SysFont(None, 30)
    my_hit_font = pygame.font.SysFont(None, 30)
    hit_text_surface = None
    main_clock = pygame.time.Clock()
    while True:
        #detect the event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == reload_mosquito_event:
                # remove mosquito and change the position
                mosquito.kill()
                # new position of mosquito
                random_x, random_y = get_random_position(WINDOW_WIDTH, WINDOW_HEIGHT, IMAGEWIDTH, IMAGEHEIGHT)
                mosquito = Mosquito(IMAGEWIDTH, IMAGEHEIGHT, random_x, random_y, WINDOW_WIDTH, WINDOW_HEIGHT)
            elif event.type == MOUSEBUTTONDOWN:
                # when user click on the mouse, check if the position of cursor is the same as the position of mosquito
                if random_x < pygame.mouse.get_pos()[0] <random_x + IMAGEWIDTH and random_y <pygame.mouse.get_pos()[1]<random_y+IMAGEHEIGHT:
                    mosquito.kill()
                    random_x, random_y = get_random_position(WINDOW_WIDTH, WINDOW_HEIGHT, IMAGEWIDTH, IMAGEHEIGHT)
                    mosquito = Mosquito(IMAGEWIDTH, IMAGEHEIGHT, random_x, random_y, WINDOW_WIDTH, WINDOW_HEIGHT)
                    hit_text_surface = my_hit_font.render('Hit', True, (0,0,0))
                    points+=1

        window_surface.fill(WHITE)

        #score board
        text_surface = my_font.render('Points: {}'.format(points), True, (0,0,0))
        window_surface.blit(mosquito.image, mosquito.rect)
        window_surface.blit(text_surface, (10, 0))

        if hit_text_surface:
            window_surface.blit(hit_text_surface, (20, 20))
            hit_text_surface = None
        pygame.display.update()
        #control the iteration speed of the game loop
        main_clock.tick(FPS)
if __name__ == '__main__':
    main()