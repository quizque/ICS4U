import pygame
from pygame.locals import *
import sys, os, math

# Config ----------------------------------------------------------#

MAX_ACTOR_HEIGHT = 658

# Setup PyGame window ---------------------------------------------#

# Setup pygame
pygame.init()

# Define window size and title
screen = pygame.display.set_mode((1170, 658))
pygame.display.set_caption('Dating Simulator')

# Define main clock
clock = pygame.time.Clock()

# Load game assets ------------------------------------------------#

def load_actor(img):
    actor = {}
    for file in os.listdir("data/images"):
        if file.startswith(img):
            tmp = pygame.image.load("data/images/" + file).convert_alpha()
            tmp = pygame.transform.scale(tmp, (math.ceil((MAX_ACTOR_HEIGHT/tmp.get_size()[1])*tmp.get_size()[0]),MAX_ACTOR_HEIGHT))
            actor[file.split("_")[len(file.split("_"))-1][:-4]] = tmp
    return actor

boy = load_actor("boy")

# Main game loop --------------------------------------------------#

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()

    screen.blit(boy["mad"], (250,250))

    pygame.display.update()

    clock.tick(60)