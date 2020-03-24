import pygame
import data.engine as e
import sys

# Load game assets ------------------------------------------------#

boy = e.load_actor("boy")
girl = e.load_actor("girl")

#e._active_actors.append(boy["default"])
#e._active_actors.append(girl["mad"])

music = e.load_audio("music", 0.05)

background = e.load_background("hallway")
e._current_background = background

music.play(-1)

# Main game loop --------------------------------------------------#

while True:

    e.pre_update()
    
    e._active_actors.append(boy["default"])
    e.draw_text_dialogbox("hoe", "this man")
    
    e._active_actors.append(girl["mad"])
    e.draw_text_dialogbox("hoe", "he is gay")
    e.draw_text_dialogbox("man", "not funny")
    e._active_actors.clear()

    e.post_update()