# If the file is being ran directly, exit
if __name__=="__main__":
    exit()

# Import pygame modules
import pygame
from pygame.locals import *

# Import mouse module
import Mouse as m

# Import other modules
import sys, os, math, textwrap

# Config ----------------------------------------------------------#

# This is the auto scale height of the
# the actors that are imported in
MAX_ACTOR_HEIGHT = 450

# PRIVATE VARIABLES -----------------------------------------------#

# Current background
_current_background = None

# Active actors
_active_actors = []

# Setup PyGame window ---------------------------------------------#

# Setup the pygame mixer
# this is done to remove the audio delay
pygame.mixer.pre_init(44100, -16, 2, 512)

# Setup pygame
pygame.init()

# Define window size and title
screen = pygame.display.set_mode((1170, 658))
pygame.display.set_caption('Dating Simulator')

# Define main clock
clock = pygame.time.Clock()

# Asset Loading Functions -----------------------------------------#

# Actor loading function
def load_actor(img):

    # Actor dictionary
    actor = {}

    # For every actor in actors...
    for file in os.listdir("data/images/actors/"):

        # if the file starts with our actors name...
        if file.startswith(img):
            
            # load in the image with alpha
            tmp = pygame.image.load("data/images/actors/" + file).convert_alpha()

            # scale so the max height is MAX_ACTOR_HEIGHT
            tmp = pygame.transform.scale(tmp, (math.ceil((MAX_ACTOR_HEIGHT/tmp.get_size()[1])*tmp.get_size()[0]),MAX_ACTOR_HEIGHT))
            
            # add to dictionary
            actor[file.split("_")[len(file.split("_"))-1][:-4]] = tmp

    # return the actor
    return actor

# Asset loading function
def load_ui_asset(img, size=(0,0)):
    # load image in with alpha
    tmp = pygame.image.load("data/images/gui/" + img + ".png").convert_alpha()

    # if size is defined, set it to the requested size
    if not (size == (0,0)):
        tmp = pygame.transform.scale(tmp, size)
    return tmp


# Background loading function
def load_background(img, size=(1170, 658)):
    # load image in with alpha
    tmp = pygame.image.load("data/images/backgrounds/" + img + ".png")

    # size image to window
    tmp = pygame.transform.scale(tmp, size)
    return tmp


# Music loading function
def load_audio(audio, volume=0.5):
    # load audio in
    tmp = pygame.mixer.Sound("data/audio/" + audio + ".ogg")
    # set audio volume to half
    # by default, audio will blow your ear drums out
    tmp.set_volume(volume)
    return tmp

# Font loading function
def load_font(font, size=20):
    # load font in at size
    tmp = pygame.font.Font("data/fonts/" + font + ".ttf", size)
    return tmp
    
# Dialog box functions --------------------------------------------#

# load in assets for dialog box
asset_dialog  = load_ui_asset("textbox")
asset_namebox = load_ui_asset("namebox")
asset_arrow   = load_ui_asset("arrow")

font_namebox  = load_font("textbox", 30)
font_textbox  = load_font("textbox", 30)

quit_title  = load_font("textbox", 30)
quit_button = load_font("textbox", 60)

# draw dialog box
# **TODO** might remove
def draw_dialogbox():
    screen.blit(asset_dialog, (177,500))

# display dialog box with text
def text_dialogbox(actor, text):

    # While user hasn't pressed next
    while True:

        # Run engine pre update
        pre_update()

        # draw background and actors
        draw_active_background()
        draw_active_actors()

        # Draw dialog box with name and text
        draw_dialogbox()
        asset_arrow.set_alpha(255)
        screen.blit(asset_arrow, (965 - math.fabs(math.sin(math.sin(pygame.time.get_ticks()/500))*10), 615))
        
        if not len(actor) == 0:
            screen.blit(asset_namebox, (195,461))
            screen.blit(font_namebox.render(actor, 1, (77, 77, 77)), (200,463))

        text = textwrap.fill(text, 45)
        c = 0
        for part in text.split('\n'):
            screen.blit(font_textbox.render(part, 1, (77, 77, 77)), (185,510 + 30*c))
            c += 1

        # If the mouse is in range and we have pressed the button once
        if m.inRange(955, 615, asset_arrow.get_size() + (10, 0)) and m.pressed_once():
            # exit loop
            return

        # Run engine post update
        post_update()



def draw_ask_dialogbox(options):
    # Used for smoothing
    prev_pos = 514

    while True:

        # Run engine pre update
        pre_update()

        # draw background and actors
        draw_active_background()
        draw_active_actors()

        # Draw dialog box with name and text
        draw_dialogbox()
        
        for i in range(len(options)):
            if m.inRange(225,505+34*i, font_textbox.size(options[i])):
                if pygame.mouse.get_pressed()[0]:
                    return options[i]
                screen.blit(font_textbox.render(options[i], 1, (255, 0, 255)), (225,506+33*i))

            else:
                screen.blit(font_textbox.render(options[i], 1, (255, 255, 255)), (225,506+33*i))

        max_v = max(min(pygame.mouse.get_pos()[1], 514 + 25*len(options)+(8*(len(options)-2))), 514+8)

        active = (max_v - prev_pos) * 0.1 + prev_pos
        prev_pos = active

        screen.blit(asset_arrow, (195, active - 8))# 615

        
        

        # Run engine post update
        post_update()

# Actor draw functions --------------------------------------------#

# draw the actors in the active list
def draw_active_actors():
    # find the about of space to spread the actors evenly
    space = 1170 / (len(_active_actors)+1)

    # for each actor
    for x in range(len(_active_actors)):
        # render them to the screen with the space
        screen.blit(_active_actors[x], (space-(_active_actors[x].get_size()[0]/2) + x * space, 104))


# Background draw functions ---------------------------------------#

# draw the active background
def draw_active_background():
    screen.blit(_current_background,(0,0))

# Button class ----------------------------------------------------#

button_hover = load_audio("hover")
button_select = load_audio("select")

class UI_Button():
    def __init__(self, pos, size, text):
        self.isPressed = False
        self.size = size
        self.pos = pos
        self.text = text
        self.isHovered = False

        self.isPressed_prev = False
        self.isHovered_prev = False
    
    def update(self):
        self.isPressed_prev = self.isPressed
        self.isHovered_prev = self.isHovered

        self.isPressed = m.inRange(self.pos[0] - self.size[0]//2, self.pos[1] - self.size[1]//2, self.size)
        self.isHovered = m.isHover(self.pos[0] - self.size[0]//2, self.pos[1] - self.size[1]//2, self.size)

        if self.isHovered and not self.isHovered_prev:
            button_hover.play()

    def draw_center(self, font, color):
        draw_textCenter(self.text, font, color, self.pos)
    
    def draw(self, font, color):
        screen.blit(font.render(self.text, 1, color), self.pos)

# Menus functions -------------------------------------------------#

def display_pauseMenu():

    # Used to generate the semi-transparent background
    s = pygame.Surface((1170, 658)) 
    s.set_alpha(175)  
    s.fill((255,255,255))

    # UI Yes/No buttons
    yes_button = UI_Button((492, 380), quit_button.size("YES"), "YES")
    no_button  = UI_Button((680, 380), quit_button.size("NO"), "NO")

    # While the pause menu is open...
    while True:

        # Run pre-update
        pre_update()

        # draw background
        draw_active_background()

        # Update the button values
        yes_button.update()
        no_button.update()

        # Draw the white overlay
        screen.blit(s, (0,0))

        # Draw the UI Box
        pygame.draw.rect(screen, (77,77,77), (398,179, 375, 300))
        pygame.draw.rect(screen, (200,200,200), (398,179, 375, 300),10)

        # Draw the UI title
        draw_textCenter("Are you sure you", quit_title, (255, 255, 255), (1170//2, 265))
        draw_textCenter("want to quit?", quit_title, (255, 255, 255), (1170//2, 295))

        # Handle user hovering the button
        if yes_button.isHovered:
            yes_button.draw_center(quit_button, (255, 0, 255))
        else:
            yes_button.draw_center(quit_button, (255, 255, 255))
        
        if no_button.isHovered:
            no_button.draw_center(quit_button, (255, 0, 255))
        else:
            no_button.draw_center(quit_button, (255, 255, 255))

        # Handle user pressing the button
        if yes_button.isPressed and pygame.mouse.get_pressed()[0]:
            button_select.play()
            pygame.quit()
            sys.exit()
        
        if no_button.isPressed and pygame.mouse.get_pressed()[0]:
            button_select.play()
            return

        # Run post update
        post_update()


# Engine functions ------------------------------------------------#

def add_actor(actor):
    _active_actors.append(actor)

def clear_actors():
    _active_actors.clear()

def draw_textCenter(text, font, color, position):
    screen.blit(font.render(text, True, color),(position[0] - font.size(text)[0]//2, position[1] - font.size(text)[1]//2))

# pre update function
# run this before drawing to the screen
def pre_update():

    # update mouse
    m.update()

    # Pygame event check for quitting
    for event in pygame.event.get():
        if event.type == QUIT:
            display_pauseMenu()

# post update function
# run this after drawing to the screen
def post_update():

    pygame.display.flip()
    clock.tick(60)
























































