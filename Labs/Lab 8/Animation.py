import pygame
import math

pygame.init()

screen = pygame.display.set_mode((750, 375))

pygame.display.set_caption("Loopy Lab")

clock = pygame.time.Clock()

done = False

img_sky = pygame.image.load("sky.jpg")
img_slime_red = pygame.image.load("slime175red.png").convert_alpha()
img_slime_green = pygame.image.load("slime175green.png").convert_alpha()
img_vball = pygame.image.load("vball.png").convert_alpha()

def clamp(value, min, max):
    if value < min:
        return min
    elif value > max:
        return  max
    else:
        return value

class Slime():
    def __init__(self, img, pos, min, max):
        self.img = img
        self.pos = pos
        self.min = min
        self.max = max

        self.v = (0,0)
        self.a = (0,20)
    
    def update(self):
        
        self.v = (self.a[0] + self.v[0], self.a[1] + self.v[1])
        print(clamp(self.v[1],0,300))
        # 0 -> 300
        self.v = (self.v[0],clamp(self.v[1],-10,10))
        
        self.pos = (self.pos[0] + self.v[0], clamp(self.pos[1] + self.v[1], 0, 263))0

    def draw(self):
        global screen
        
        screen.blit(self.img, self.pos)

green_slime = Slime(img_slime_green, (0,0), 0, 300)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Background
    screen.blit(img_sky, (0,0))
    pygame.draw.rect(screen,(204, 170, 102),(0,301,750,73))
    pygame.draw.rect(screen,(255, 255, 255),(373,264,4,42))

    # Update Elements
    green_slime.update()

    # Draw elements
    green_slime.draw()

    pygame.display.flip()

    clock.tick(60)