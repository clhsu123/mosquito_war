import sys
import pygame

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

        

