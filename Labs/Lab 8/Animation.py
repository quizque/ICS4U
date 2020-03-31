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

class PID():
    def __init__(self, p, i, d):
        self.p = p
        self.i = i
        self.d = d
        self.prev_error = 0
        self.prev_value = 0
        self.prev_time = pygame.time.get_ticks()

    def p_c(self, error):
        return self.p * error

    def i_c(self, error):
        return 0

    def d_c(self, error):
        return self.d * (error/(pygame.time.get_ticks()- self.prev_time))
    
    def calc(self, input):
        error = input - self.prev_value
        value = self.p_c(error) + self.i_c(error) + self.d_c(error-self.prev_error)
        print(error, value)

        self.prev_value = value
        self.prev_error = error
        self.prev_time = pygame.time.get_ticks()
        return value

class Slime():
    def __init__(self, img, pos, min, max):
        self.img = img
        self.pos = pos
        self.min = min
        self.max = max
        self.pid = PID(0.0075,0,2.25)

        self.v = (0,0)
        self.a = (0,20)
    
    def update(self):

        self.v = (self.a[0] + self.v[0], self.a[1] + self.v[1])


        # FOLLOW MOUSE
        t = self.pid.calc(pygame.mouse.get_pos()[0]-self.pos[0])
        self.v = (self.v[0] + t, self.v[1])

        # 0 -> 300
        self.v = (clamp(self.v[0],-10, 10),clamp(self.v[1],-10,10))
        self.pos = (clamp(self.pos[0] + self.v[0], self.min, self.max), clamp(self.pos[1] + self.v[1], 0, 263))

    def draw(self):
        global screen
        
        screen.blit(self.img, (self.pos[0]-37, self.pos[1]))

green_slime = Slime(img_slime_green, (0,262), 37, 334)
red_slime = Slime(img_slime_red, (560,262), 413, 712)

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
    red_slime.update()

    # Draw elements
    green_slime.draw()
    red_slime.draw()

    pygame.display.flip()

    clock.tick(60)