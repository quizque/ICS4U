import pygame

# Actor expression constants
EXPRESSION_DEFAULT = 0
EXPRESSION_HAPPY   = 1
EXPRESSION_UPSET   = 2


# Actor class
class Actor(pygame.sprite.Sprite):

    def __init__(self, _position, _scale, _expression_list):
        
        # Initialize the sprite class
        super().__init__()
        
        # Define the position, scale, and rotation of the actor
        self.position = _position
        self.scale = _scale
        self.expression_list = []

        for image_path in _expression_list:
            tmp_img = pygame.image.load(image_path)
            
            self.expression_list.append(pygame.transform.scale(tmp_img.convert_alpha(), (int(tmp_img.get_width()*self.scale), int(tmp_img.get_height()*self.scale))))

        self.image = self.expression_list[EXPRESSION_DEFAULT]
        self.rect = self.image.get_rect()