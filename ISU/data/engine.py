if __name__=="__main__":
    exit()

import pygame
from pygame.locals import *
import data.mouse as m
import sys, os, math

# Config ----------------------------------------------------------#

MAX_ACTOR_HEIGHT = 450

# PRIVATE VARIABLES -----------------------------------------------#

_current_background = None
_active_actors = []

# Setup PyGame window ---------------------------------------------#

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
    actor = {}
    for file in os.listdir("data/images/actors/"):
        if file.startswith(img):
            tmp = pygame.image.load("data/images/actors/" + file).convert_alpha()
            tmp = pygame.transform.scale(tmp, (math.ceil((MAX_ACTOR_HEIGHT/tmp.get_size()[1])*tmp.get_size()[0]),MAX_ACTOR_HEIGHT))
            actor[file.split("_")[len(file.split("_"))-1][:-4]] = tmp
    return actor

# Asset loading function
def load_ui_asset(img, size=(0,0)):
    tmp = pygame.image.load("data/images/gui/" + img + ".png").convert_alpha()
    if not (size == (0,0)):
        tmp = pygame.transform.scale(tmp, size)
    return tmp

# Background loading function

def load_background(img, size=(1170, 658)):
    tmp = pygame.image.load("data/images/backgrounds/" + img + ".png")
    tmp = pygame.transform.scale(tmp, size)
    return tmp

# Music loading function

def load_audio(audio, volume=0.5):
    tmp = pygame.mixer.Sound("data/audio/" + audio + ".ogg")
    tmp.set_volume(volume)
    return tmp

# Font loading function
def load_font(font, size=20, bold=False):
    tmp = pygame.font.Font("data/fonts/" + font + ".ttf", size)
    tmp.set_bold(bold)
    return tmp
    
# Dialog box functions --------------------------------------------#

asset_dialog  = load_ui_asset("textbox")
asset_namebox = load_ui_asset("namebox")
asset_arrow   = load_ui_asset("arrow")
font_namebox  = load_font("textbox", 30)
font_textbox  = load_font("textbox", 30)
audio_select  = load_audio("select")
audio_hover   = load_audio("hover")

def draw_dialogbox():
    screen.blit(asset_dialog, (177,500))

def draw_text_dialogbox(actor, text):
    tmp_running = True
    while tmp_running:
        pre_update()

        draw_dialogbox()
        screen.blit(asset_namebox, (195,465))
        screen.blit(asset_arrow, (965, 615))
        screen.blit(font_namebox.render(actor, 1, (77, 77, 77)), (200,467))
        screen.blit(font_textbox.render(text, 1, (77, 77, 77)), (190,510))

        #if m.isHover(965, 615, asset_arrow.get_size()):
        if m.isHover_once(965, 615, asset_arrow.get_size()):
            audio_hover.play()

        if m.inRange(965, 615, asset_arrow.get_size()) and m.pressed_once():
            audio_select.play()
            tmp_running = False

        post_update()


# Actor draw functions --------------------------------------------#

def draw_active_actors():
    space = 1170 / (len(_active_actors)+1)
    for x in range(len(_active_actors)):
        screen.blit(_active_actors[x], (space-(_active_actors[x].get_size()[0]/2) + x * space, 104))


# Background draw functions ---------------------------------------#

def draw_active_background():
    screen.blit(_current_background,(0,0))

# Engine functions ------------------------------------------------#

def pre_update():
    m.update()

    draw_active_background()
    draw_active_actors()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()

def post_update():

    pygame.display.update()
    clock.tick(60)
























































