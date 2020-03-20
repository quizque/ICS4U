import pygame
from pygame.locals import *
import data.engine as e
import sys

# Load game assets ------------------------------------------------#

boy = e.load_actor("boy")
girl = e.load_actor("girl")

e._active_actors.append(boy["default"])
e._active_actors.append(girl["mad"])

music = e.load_audio("music", 0.05)

background = e.load_background("hallway")
e._current_background = background

music.play()

# Main game loop --------------------------------------------------#

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()

    e.draw_active_background()

    e.draw_active_actors()

    e.draw_text_dialogbox("hoe", "this man")

    e.update()