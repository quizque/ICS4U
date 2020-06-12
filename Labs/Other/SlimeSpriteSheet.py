import sys
 
import pygame
import math
from pygame.locals import *
 
pygame.init()

fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))
 
# Spritesheet class
# takes in the ALREADY LOADED sheet
# and how many columns (frames) there are
class Spritesheet():

    def __init__(self, _sheet, _columns):
        # Used to make sure every frame is the same size
        if (_sheet.get_size()[0] // _columns) != (_sheet.get_size()[0] / _columns):
            print("[ERROR] Spritesheet size is inconsistent!")
            pygame.quit()
            sys.exit()

        # Store the sheet
        self.sheet = _sheet

        # Store the columns
        self.columns = _columns

        # How big is each frame in the x?
        self.frame_size_x = _sheet.get_size()[0] / _columns

        # How big is each frame in the y?
        self.frame_size_y = _sheet.get_size()[1]

    # Draw a frame from the sprite sheet
    def drawFrame(self, _surface, _frame, _position):
        # Draw the frame at the required position
        _surface.blit(self.sheet, _position, (_frame*self.frame_size_x,0,self.frame_size_x,self.frame_size_y))


class Slime():
    def __init__(self, _position):
        # Sprite sheet of the default walk animation
        self.default_spritesheet = Spritesheet(pygame.image.load("spritesheet.png").convert_alpha(), 5)

        # Position of the slime
        self.position = _position

        # Current frame of the walk cycle
        self.walk_current_frame = 0
        # Used to keep track of when to update the current frame
        self.walk_last_update = 0
        # The frames on the sprite sheet that
        # hold the walk cycle
        self.walk_animation = [0,1,2,3]

        # Is the slime hurt?
        self.is_hurt = False
        # Used keep the slime in "hurt" for a little bit
        self.hurt_counter = 0
        # Holds the frame where the "hurt" frame is
        self.hurt_animation = 4

    # Update the slimes status (like hp, is hurt, etc.)
    def update(self):

        # If we are hurt, check to see if we aren't anymore
        if self.is_hurt:
            # Had the required time passed?
            if pygame.time.get_ticks() >= self.hurt_counter:
                self.is_hurt = False

        # Update our walk cycle
        # but only when we aren't hurt
        # and only every 100 ms
        if self.is_hurt == False and pygame.time.get_ticks() > self.walk_last_update:

            # Increase the current frame
            self.walk_current_frame += 1

            # Make sure we don't go outside of the animation array
            if self.walk_current_frame > len(self.walk_animation)-1:
                # If we are, though, set it back to the first frame
                self.walk_current_frame = 0
            
            # Increase the counter another 100 ms
            # the "recommend" stupid way because pygame is fucked
            self.walk_last_update = pygame.time.get_ticks() + 100

    # Make the slime take damage!
    def hit(self, _damage):
        # Print Damage
        print("[INFO] Did " + str(_damage) + " damage!")

        # We are now hurt
        self.is_hurt = True

        # Lets stay hurt for 500ms (or 0.5s)
        self.hurt_counter = pygame.time.get_ticks() + 500

    # Draw the slime
    def draw(self, _surface):

        # Are we hurt?
        if self.is_hurt:
            # Draw hurt frame
            self.default_spritesheet.drawFrame(_surface, self.hurt_animation, self.position)
        
        # Otherwise, draw walk animation
        else:
            self.default_spritesheet.drawFrame(_surface, self.walk_current_frame, self.position)

# Define a slime :O
one_slime = Slime((0,0))

# To make sure mouse only fires once
prev_mouse = False

while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Make slime bounce :O
    one_slime.position = (100, math.sin(pygame.time.get_ticks()/400)*100+100)

    # Check to make sure we are 1. pressing the mouse 2. wern't pressing it previously 3. the slime isn't hurt
    if pygame.mouse.get_pressed()[0] and not prev_mouse and not one_slime.is_hurt:
        # Hit the slime :(
        one_slime.hit(55)

    # Update the slime :O
    one_slime.update()

    # Draw the slime :O
    one_slime.draw(screen)

    # Update prev mouse
    prev_mouse = pygame.mouse.get_pressed()[0]

    pygame.display.flip()
    fpsClock.tick(60)