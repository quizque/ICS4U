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
    
    #e._active_actors.append(boy["default"])
    e.draw_text_dialogbox("???", "Hey, what makes you think you can barge in on my turf!?")
    
    e._active_actors.append(boy["default"])
    e.draw_text_dialogbox("???", "I'm just kidding.")
    
    e.draw_text_dialogbox("Duncan", "Hi, i'm Duncan. No need to run away scared. Welcome to the school. What class do you have?")
    
    e.draw_text_dialogbox("", "I have no idea, uh looks like uh...")

    e.draw_text_dialogbox("Duncan", "You are with Mr. Veeman on the third floor... room 368")
    e.draw_text_dialogbox("Duncan", "Want me to walk you there?")
    e._active_actors.clear()

    e.post_update()