import pygame

EXPRESSION_DEFAULT = 0
EXPRESSION_HAPPY   = 1
EXPRESSION_UPSET   = 2

class Actor():

    def __init__(self, _position, _scale, _expression_list):
        self.position = _position
        self.scale = _scale
        self.expression_list = []

        for image_path in _expression_list:
            tmp_img = pygame.image.load(image_path)
            
            self.expression_list.append(pygame.transform.scale(tmp_img.convert(), (tmp_img.get_width(), tmp_img.get_height())))

    def draw(self, screen):
        ...