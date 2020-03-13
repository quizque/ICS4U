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
        
        # Define the scale of the actor
        self.scale = _scale
        
        self.expression_list = []

        for image_path in _expression_list:
            tmp_img = pygame.image.load(image_path)
            
            self.expression_list.append(pygame.transform.scale(tmp_img.convert_alpha(), (int(tmp_img.get_width()*self.scale), int(tmp_img.get_height()*self.scale))))

        self.image = self.expression_list[EXPRESSION_DEFAULT]
        self.rect = self.image.get_rect()

        # Recalculate the position
        self.rect[0] = _position[0] - (self.rect[2]//2)
        self.rect[1] = _position[1] - (self.rect[3]//2)

    def inRange(_position):
        if (self.rect[0] <= _position[0] <= (self.rect[0] + self.rect[2])):
            if (self.rect[1] <= _position[1] <= (self.rect[1] + self.rect[3])):
                return True
        return False
