import pygame
import Engine as e
import sys

# Load game assets ------------------------------------------------#

boy = e.load_actor("boy")
girl = e.load_actor("girl")

#e._active_actors.append(boy["default"])
#e._active_actors.append(girl["mad"])

music = e.load_audio("music", 0.05)

background = e.load_background("hallway")

music.play(-1)

# Main game loop --------------------------------------------------#

while True:

    e._current_background = background
    
    

    e.text_dialogbox("???", "Hey, what makes you think you can barge in on my turf!?")
    
    e.add_actor(boy["default"])
    e.text_dialogbox("???", "I am pooping my pants")

    input_t = e.draw_ask_dialogbox(["( ͡° ͜ʖ ͡°)", "ewwwww!"])

    if input_t == "*poop pants too*":
        e.text_dialogbox("Duncan", "Kinky")
    
    e.text_dialogbox("Duncan", "Hi, i'm Duncan. No need to run away scared. Welcome to the school. What class do you have?")
    
    e.text_dialogbox("", "I have no idea, uh looks like uh...")

    e.text_dialogbox("Duncan", "You are with Mr. Veeman on the third floor... room 368")
    e.text_dialogbox("Duncan", "Want me to walk you there?")
    e.clear_actors()