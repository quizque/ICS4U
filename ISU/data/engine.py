import pygame
import sys, os, math

# Config ----------------------------------------------------------#

MAX_ACTOR_HEIGHT = 450

# PRIVATE VARIABLES -----------------------------------------------#

_current_background = None
_active_actors = []

# Setup PyGame window ---------------------------------------------#

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
    for file in os.listdir("data/images"):
        if file.startswith(img):
            tmp = pygame.image.load("data/images/" + file).convert_alpha()
            tmp = pygame.transform.scale(tmp, (math.ceil((MAX_ACTOR_HEIGHT/tmp.get_size()[1])*tmp.get_size()[0]),MAX_ACTOR_HEIGHT))
            actor[file.split("_")[len(file.split("_"))-1][:-4]] = tmp
    return actor

# Asset loading function
def load_asset(img, size=(0,0)):
    tmp = pygame.image.load("data/images/" + img + ".png").convert_alpha()
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

asset_dialog  = load_asset("textbox")
asset_namebox = load_asset("namebox")
font_namebox  = load_font("textbox", 30)
font_textbox  = load_font("textbox", 30)

def draw_dialogbox():
    screen.blit(asset_dialog, (177,500))

def draw_text_dialogbox(actor, text):
    draw_dialogbox()
    screen.blit(asset_namebox, (195,465))
    screen.blit(font_namebox.render(actor, 1, (77, 77, 77)), (200,467))
    screen.blit(font_textbox.render(text, 1, (77, 77, 77)), (190,510))


# Actor draw functions --------------------------------------------#

def draw_active_actors():
    space = 1170 / (len(_active_actors)+1)
    for x in range(len(_active_actors)):
        screen.blit(_active_actors[x], (space-(_active_actors[x].get_size()[0]/2) + x * space, 104))


# Background draw functions ---------------------------------------#

def draw_active_background():
    screen.blit(_current_background,(0,0))

# Engine functions ---------------------------------------#

def update():
    pygame.display.update()
    clock.tick(60)
























































