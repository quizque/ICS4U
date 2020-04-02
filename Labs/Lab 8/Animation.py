#********************************************************************************
#** Nick Coombe 2020/03/25 ***
#** Lab 8 Introduction to Animation ***
#** ***
#** Display two slimes bouncing a ball back and fourth. ***
#** Complete with physics and tracking eyes. ***
#** ***
#********************************************************************************

import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((750, 375))

pygame.display.set_caption("Slime Animation")

clock = pygame.time.Clock()

done = False

# Image Loading ---------------------------------------------------#

# Import all of the require images
# convert_alpha() preserves transparency
img_sky = pygame.image.load("sky.jpg")
img_slime_red = pygame.image.load("slime175red.png").convert_alpha()
img_slime_green = pygame.image.load("slime175green.png").convert_alpha()
img_vball = pygame.image.load("vball.png").convert_alpha()

# Classes and Functions -------------------------------------------#

# Clamp the input between two numbers
# INPUTS
#   - Input Number (int)
#   - Minimum Number (int)
#   - Maximum Number (int)
# OUTPUT
#   - Clamped result { min <= in <= max } (int)
def clamp(value, min, max):
    if value < min:
        return min
    elif value > max:
        return  max
    else:
        return value


# Class for processing the slimes
class Slime():
    # Constructor
    def __init__(self, img, pos, min, max):
        self.img = img # image
        self.pos = pos # position

        # Used to keep the slime between one spot
        self.min = min # x-minimum
        self.max = max # x-maximum

        # Velocity
        self.v = (0,0)

        # Acceleration
        self.a = (0,20)
    
    # Update the physics
    def update(self, ball):

        # Add acceleration to velocity
        self.v = (self.a[0] + self.v[0], self.a[1] + self.v[1])

        # Update position and clamp velocity and position
        # 0 -> 300
        self.v = (clamp(self.v[0],-10, 10),clamp(self.v[1],-10,10))
        self.pos = (clamp(ball.get_position()[0], self.min, self.max), clamp(self.pos[1] + self.v[1], 0, 263))

    # Draw the slime
    def draw(self, ball_loc):
        # Accessed the global screen
        global screen
        
        # Draw image to screen
        screen.blit(self.img, (self.pos[0]-37, self.pos[1]))

        # Draw eye outline
        pygame.draw.circle(screen, (255,255,255), (self.pos[0], self.pos[1]+15), 10)

        # Find the x/y difference to calculate eye position
        x_dif = ball_loc[0] - self.pos[0]
        y_dif = ball_loc[1] - self.pos[1]  + 15
        if x_dif == 0:
            x_dif = 0.00001

        # Find the angle from the eye to the ball
        result = (math.atan2(y_dif,x_dif))
        
        # Draw the eye relative to the angle from before
        pygame.draw.circle(screen, (0,0,0), (self.pos[0] + math.floor(math.cos(result)*5), self.pos[1]+15 + math.floor(math.sin(result)*5)), 3)

# Class for processing the ball
class Ball():
    # Constructor
    def __init__(self, img, pos):
        self.img = img
        self.pos = pos

        self.v = (35,-20)
        self.a = (0,5)

    # Return the current position
    def get_position(self):
        return self.pos
    
    # Update the physics
    def update(self):

        # Add acceleration to velocity
        self.v = (self.a[0] + self.v[0], self.a[1] + self.v[1])

        # Clamp velocity
        # 0 -> 300
        self.v = (clamp(self.v[0],-15, 15),clamp(self.v[1],-40,40))

        ## Collition detection for the roof, floor and sides
        # Also add a little random velocity to make it more intresting
        # the "bounce" effect is done just by reversing the velocity in that direction
        if self.pos[1] >= 248:
            self.v = (self.v[0], -self.v[1] + random.randint(-2,2))
        if self.pos[1] <= 0:
            self.v = (self.v[0], -self.v[1] + random.randint(-2,2))
        if self.pos[0] <= 0:
            self.v = (-self.v[0] + random.randint(-8,8), self.v[1])
        if self.pos[0] >= 725:
            self.v = (-self.v[0] + random.randint(-8,8), self.v[1])

        # Update and clamp the position
        self.pos = (clamp(self.pos[0] + self.v[0], 0, 725), clamp(self.pos[1] + self.v[1], 0, 248))

    # Draw the ball to the screen
    def draw(self):
        # Call for the global screen
        global screen
        
        screen.blit(self.img, (self.pos[0], self.pos[1]))

# Main Function ---------------------------------------------------#        

# Define the slime and volleyball
green_slime = Slime(img_slime_green, (0,262), 37, 334)
red_slime = Slime(img_slime_red, (560,262), 413, 712)
vball = Ball(img_vball, (0,100))

# while we haven't quit
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Background
    screen.blit(img_sky, (0,0))
    pygame.draw.rect(screen,(204, 170, 102),(0,301,750,73))
    pygame.draw.rect(screen,(255, 255, 255),(373,264,4,42))

    # Update Elements
    green_slime.update(vball)
    red_slime.update(vball)
    vball.update()

    # Draw elements
    green_slime.draw(vball.pos)
    red_slime.draw(vball.pos)
    vball.draw()

    pygame.display.flip()

    clock.tick(30)