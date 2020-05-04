import pygame

# Textbox Class ---------------------------------------------------#

class Textbox(pygame.sprite.Sprite):


    def __init__(self, color):
       pygame.sprite.Sprite.__init__(self)
       
       self.image = pygame.Surface([width, height])
       self.image.fill(color)
       
       self.rect = self.image.get_rect()