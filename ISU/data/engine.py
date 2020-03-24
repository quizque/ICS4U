# If the file is being ran directly, exit
if __name__=="__main__":
    exit()

# Import pygame modules
import pygame
from pygame.locals import *

# Import mouse module
import data.mouse as m

# Import other modules
import sys, os, math

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
audio_select  = load_audio("select")
audio_hover   = load_audio("hover")

# draw dialog box
# **TODO** might remove
def draw_dialogbox():
    screen.blit(asset_dialog, (177,500))

# display dialog box with text
def draw_text_dialogbox(actor, text):

    # While user hasn't pressed next
    tmp_running = True
    while tmp_running:

        # Run engine pre update
        pre_update()

        # Draw dialog box with name and text
        draw_dialogbox()
        screen.blit(asset_namebox, (195,465))
        screen.blit(asset_arrow, (965, 615))
        screen.blit(font_namebox.render(actor, 1, (77, 77, 77)), (200,467))
        screen.blit(font_textbox.render(text, 1, (77, 77, 77)), (190,510))

        # If the mouse is hovering over the "next" arrow and we haven't ran this yet
        if m.isHover_once(965, 615, asset_arrow.get_size()):
            # play hover audio
            audio_hover.play()

        # If the mouse is in range and we have pressed the button once
        if m.inRange(965, 615, asset_arrow.get_size()) and m.pressed_once():

            # play the audio
            audio_select.play()

            # exit loop
            tmp_running = False

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

# Engine functions ------------------------------------------------#

# pre update function
# run this before drawing to the screen
def pre_update():

    # update mouse
    m.update()

    # draw background and actors
    draw_active_background()
    draw_active_actors()

    # Pygame event check for quitting
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()

# post update function
# run this after drawing to the screen
def post_update():

    pygame.display.update()
    clock.tick(60)
























































