#Hey Nick the bugs I was having trouble with were at the end of p2 going into p3 u only see the start of the history class if u select Stevey in p2
#Other one was if u follow candace at the start u eventually are just sent back to school for some reason
import pygame
import engine as e
import sys

# Load game assets ------------------------------------------------#

boy = e.load_actor("boy")
girl = e.load_actor("girl")
arn = e.load_actor("arn")
trix = e.load_actor("trix")
vee = e.load_actor("vee")
ste = e.load_actor("ste")
bono = e.load_actor("bono")
#e._active_actors.append(boy["default"])
#e._active_actors.append(girl["mad"])

music = e.load_audio("music", 0.05)

background = e.load_background("hallway")
menu = e.load_background("Bed")
classroom = e.load_background("classroom")
field = e.load_background("field")
music.play(-1)

#sterotype

bad = 0
good = 0
wrong = 0
right = 0

#class 2
p2 = 0
classp2 = 0
p3 = 0


#POSSIBLE LOVES (Star next means healthy)
#Duncan*
#Issac
#Linnesay*
#Britnay
#Stevey
Dun = 0
Iss = 0
Lin = 0
Bri = 0
Ste = 0

# Main game loop --------------------------------------------------#

#Jakob Wrote story and all choices
#nick Made engine
#Chris did sounds and images
#Paolo did the editing and some minor  bug fixes


while True:


    e._current_background = menu
    e.text_dialogbox("Narrator", "Welcome To Highschool Simulator where you will be able to make choices and decide your fate")
    e.text_dialogbox("Narrator", "To play you click the arrow at the bottom right and when a choice comes up you click on the one you decide on")
    e.text_dialogbox("Narrator", "You just moved to the beautiful town of Famaria but its the middle of the year and a new school means new possibilities!")
    input_q = e.draw_ask_dialogbox(["Ready to start", "Tutorial again"])
    
    if input_q == "Ready to start":

        # To do a fade, first you call fade in,
        e.fade_in_card("Dawn of The First Day", "-48 Hours Remain-")

        # Then change the background
        e._current_background = background

        # Then fade out
        e.fade_out_card("Dawn of The First Day", "-48 Hours Remain-")

        e._current_background = background
        
        

            
        e.text_dialogbox("Narrator", "You Finally make it to school but you dont know where your class is. there are two students up ahead")
        e.add_actor(boy["default"])
        e.add_actor(girl["default"])
        input_t = e.draw_ask_dialogbox(["Ask Boy for help", "Ask Girl for help"])
            
            
            


        e.clear_actors()

        if input_t == "Ask Boy for help":
            e.add_actor(boy["mad"])
            e.text_dialogbox("???", "Hey, what makes you think you can barge in on my turf!?")
            e.clear_actors()
            e.add_actor(boy["default"])
            e.text_dialogbox("???", "Im just fooling around")
            e.text_dialogbox("Duncan", "Hi, i'm Duncan. No need to run away scared. Welcome to the school. What class do you have?")
            e.text_dialogbox("", "I have no idea, uh looks like uh...")
            e.text_dialogbox("Duncan", "You are with Mr. Veeman on the third floor... room 368")
            e.text_dialogbox("Duncan", "Want me to walk you there?")
            input_u = e.draw_ask_dialogbox(["Yes", "No"])

            if  input_u == "Yes":
                e.text_dialogbox("Duncan", "Ok sweet lets go")
                e.text_dialogbox("Duncan", "I know your new but That girl over there is Britney She sucks")
                e.text_dialogbox("Duncan", "Ok heres your class see you later Ill be sitting in the Caf at lunch")
                e.clear_actors()
                good += 1
                Dun += 1
            elif input_u == "No":
                e.text_dialogbox("Duncan", "Ok See ya later then, its up ahead on your left")
                e.clear_actors()
                good += 1
                    
        elif input_t == "Ask Girl for help":
            e.add_actor(girl["mad"])
            e.text_dialogbox("", "Hello?")
            e.clear_actors()
            e.add_actor(girl["default"])
            e.text_dialogbox("???", "Are you talking to me?")
            e.text_dialogbox("???", "You have no idea who I am")
            e.text_dialogbox("", "um, Im new here and...")
            e.text_dialogbox("???", "You stay away from me and my people you cant handle hanging out with me.")
            e.add_actor(boy["default"])
            e.text_dialogbox("???", "um,, Hey leave her alone. Come with me")
            e.text_dialogbox("Britney", "Im Britney remember that , Now scram unless you think you can be one of us.")    
            input_y = e.draw_ask_dialogbox(["Stay with Britney", "Go with boy"])
            e.clear_actors()
                
            if input_y == "Go with boy":
                e.add_actor(boy["default"])
                e.text_dialogbox("", "Uh thanks for helping me that girl is a uh...")
                e.text_dialogbox("Duncan", "A Meanie. Hi, i'm Duncan. No need to run away scared. Welcome to the school. What class do you have?")
                e.text_dialogbox("", "I have no idea, uh looks like uh...")
                e.text_dialogbox("Duncan", "You are with Mr. Veeman on the third floor... room 368")
                e.text_dialogbox("Duncan", "Want me to walk you there?")
                input_u = e.draw_ask_dialogbox(["Yes", "No"])

                if  input_u == "Yes":
                        e.text_dialogbox("Duncan", "Ok sweet lets go")
                        e.text_dialogbox("Duncan", "I know your new but That girl over there is Britney She sucks")
                        e.text_dialogbox("Duncan", "Ok heres your class see you later Ill be sitting in the Caf at lunch")
                        e.clear_actors()
                        good += 1
                        Dun += 1
                elif input_u == "No":
                        e.text_dialogbox("Duncan", "Ok See ya later then its up ahead on your left")
                        e.clear_actors()
                        good += 1
                    
            elif input_y == "Stay with Britney":
                e.add_actor(boy["default"])
                e.add_actor(girl["default"])
                e.text_dialogbox("", "Im fine I'll be staying with Britney")
                e.text_dialogbox("Duncan","Oh Ok bye Im Duncan by the way")
                e.clear_actors()
                e.add_actor(girl["happy"])
                e.text_dialogbox("Britney","Oh you have Veeman first period he is awful lets skip!")
                input_i = e.draw_ask_dialogbox(["Skip class and hangout with the cool kids", "Look for class"])
                bad += 1
                Bri += 1
                e.clear_actors()
                    
                if input_i == "Look for class":
                    e.add_actor(girl["default"])
                    e.text_dialogbox("", "Ug I cant do that bye")
                    e.text_dialogbox("Britney", "Never talk to me again")
                    e.text_dialogbox("Narrator", "You find yourself lost and get to class 20 minutes late")
                    
                    e.clear_actors()
                        
                elif input_i == "Skip class and hangout with the cool kids":
                    bad += 1
                    e.add_actor(girl["happy"])
                    e.text_dialogbox("", "Ok lets do this")
                    e.text_dialogbox("Britney", "Maybe you are cool lets go!")
                    Bri += 1

# CHUNK 1 FIRST SPLIT 


        #*****************GO TO CLASS PATH******************** 

        if good > 0:
            e.clear_actors()
            e._current_background = classroom                            
            e.text_dialogbox("Narrator", " You enter Mr.Veemans class and you suddenly feel Queasy. The teacher looks like a sweaty hog as he snorts for you to sit. ")
            
            e.text_dialogbox("Narrator","There are two spots open one in the back with a red headed boy and one in the front with a black haired girl")
            e.add_actor(arn["default"])
            e.add_actor(trix["default"])
            input_i = e.draw_ask_dialogbox(["Sit with redhead", "Sit with black haired"])
            e.clear_actors()
            
            if input_i == "Sit with redhead":
                e.add_actor(arn["default"])
                e.text_dialogbox("Narrator","You sit next to the redhead he appears to be a nerd he smells slightly of B.O.")
                e.text_dialogbox("Narrator","Its is managable")
                e.text_dialogbox("Issac","Hey my name is Issac but my colleagues call me nerdy 4 eyes")
                e.text_dialogbox("Nerdy 4 eyes","But I'm fine with it")
                input_i = e.draw_ask_dialogbox(["muster through", "Beauty sleep"])

                if input_i == "muster through":
                    e.text_dialogbox("Narrator","you muster through class even though it being difficult")
                    e.text_dialogbox("Nerdy","*Blushing* Woah you were paying attention to that boring lesson all I could pay attention was your plump brain")
                    e.text_dialogbox("Narrator","The bell rings and you go to period 2")
                    e.clear_actors()
                    Iss += 1
                    p2 += 1
                    
                elif input_i == "Beauty sleep":
                    e.text_dialogbox("Narrator","you fall asleep and when you wake up your being stared at")
                    e.text_dialogbox("Nerdy","woah you are a dork")
                    e.text_dialogbox("Narrator","The bell rings and you go to period 2 after being yelled at by Mr V")
                    e.clear_actors()
                    p2 += 1
                
            

            elif input_i == "Sit with black haired":
                e.add_actor(trix["default"])
                e.text_dialogbox("Narrator","you sit next to the girl")
                e.text_dialogbox("","Hello?")
                e.text_dialogbox("Narrator","she slowly turns her head at you. ")
                e.text_dialogbox("Linnesay","Im Linnesay What do you like need uh....")
                input_h = e.draw_ask_dialogbox(["Chat with her", "Do your work"])
                
                if input_h == "Chat with her":
                    e.text_dialogbox("Narrator","you look at her and try to start a conversation")
                    e.text_dialogbox("Linnesay","Uh...hello...I'm linnesay with two n's")
                    e.text_dialogbox("","Oh thats cool")
                    e.add_actor(vee["mad"])
                    e.text_dialogbox("Mr Veeman","New Kid be quiet I am doing attendance!")
                    e.clear_actors()
                    Lin += 1
                    input_i = e.draw_ask_dialogbox(["Yell loudly", "Comply"])
                
                    
                    if input_i == "Yell loudly":
                        e.add_actor(vee["mad"])
                        e.text_dialogbox("Mr Veeman","New Kid Im SENDING YOU HOME!")
                        e.clear_actors()
                        bad += 2

                    elif input_i == "Comply":
                        e.text_dialogbox("Narrator","Linnesay seems happy you didnt do somthing dumb")
                        e.text_dialogbox("Narrator","Class ends")
                        p2 += 1
                    
                elif input_h == "Do your work":
                    e.text_dialogbox("Narrator","you work hard and decide to leave the girl alone")
                    
                    e.text_dialogbox("Linnesay","Working hard there. oof i got stuck with a nerd its the first day")
                    e.text_dialogbox("Narrator","You feel smarter and made good notes")
                    e.text_dialogbox("Narrator","You get up and get ready for period 2")
                    e.clear_actors()
                    p2 += 1
                

        #******************SKIP CLASS PATH*************************    
        elif bad > 0:
            e._current_background = field    
            e.text_dialogbox("Narrator", "You ditch school and talk about usueless stuff with Britney and her friends")
            e.add_actor(girl["default"])
            e.add_actor(girl["mad"])
            e.add_actor(girl["happy"])
            e.text_dialogbox("Narrator", "The bell rings but as that happens a teacher apporaches")
            e.text_dialogbox("Britney", "Can you distract the teach and take the blame for us?")
            input_i = e.draw_ask_dialogbox(["Take blame", "Run away","cry and beg for forgiveness"])

            if input_i == "Take blame":
                e.clear_actors()
                e.text_dialogbox("Narrator", "You save Britney by lying and saying only you skipped you get sent home from school")
                e.text_dialogbox("Narrator", "Day 1 Complete")
                e.clear_actors()
                Bri += 1
                bad += 1
                # To do a fade, first you call fade in,
                e.fade_in_card("Dawn of The Second Day", "-48 Hours Remain-")
                

        # Then change the background
                e._current_background = background

        # Then fade out
                e.fade_out_card("Dawn of The Second Day", "-48 Hours Remain-")

                e._current_background = background
                

                
            elif input_i == "Run away":
                e.clear_actors()
                e.add_actor(girl["default"])
                e.add_actor(girl["mad"])
                e.text_dialogbox("Narrator", "You run away and a random girl takes the fall Britney gives you a look")
                e.text_dialogbox("Narrator", "You go to period 2")
                Bri += 1
                e.clear_actors()
                p2 += 1

            elif input_i == "cry and beg for forgiveness":
               
                e.clear_actors()
                e.text_dialogbox("Narrator", "You cry and beg for forgiveness . Britney and her friends get sent home and you get sent to your second class")
                e.clear_actors()
                p2 += 1


        #****PART 2 Of DAY 1****
        if p2 > 0:

            e.text_dialogbox("Narrator", "You walk down the hall to go to period 2")
            e.text_dialogbox("Narrator", "On the way you see that a small boy dropped his phone")
            input_i = e.draw_ask_dialogbox(["Help Small", "Walk with Issac","Straight to class","Walk with Linnesay"])

            if input_i == "Help Small":
                    e.text_dialogbox("Narrator", "You walk down the hall and pick up smalls phone")
                    e.add_actor(boy["default"])
                    e.text_dialogbox("Narrator", "He turns around and its Duncan")
                    e.text_dialogbox("Duncan", "Hey thanks lets walk to your class")
                    e.clear_actors()
                    Dun += 1
                    classp2 += 1

            elif input_i == "Walk with Issac":
                    e.text_dialogbox("Narrator", "You walk down the hall and ask Issac to walk with you")
                        
                    if Iss > 0:
                            e.add_actor(arn["default"])
                            e.text_dialogbox("Issac", "Yeah Dummy Dumb lets go")
                            e.text_dialogbox("Narrator", "You walk to Period 2 with Issac")
                            e.clear_actors()
                            Iss += 1
                            classp2 += 1

                    else:
                            e.add_actor(arn["default"])
                            e.text_dialogbox("Issac", "Go away")
                            e.text_dialogbox("Narrator", "You walk to Period 2 alone")
                            classp2 += 1
                            Iss += 1
                            e.clear_actors()

            elif input_i == "Straight to class":
                    e.text_dialogbox("Narrator", "You walk down the hall to go to period 2")
                    classp2 += 1
                    e.clear_actors()


            elif input_i == "Walk with Linnesay":
                    e.text_dialogbox("Narrator", "You walk down the hall to go to period 2")

                    if Lin > 0:
                            e.add_actor(trix["default"])
                            e.text_dialogbox("Linnesay", "Yeah sure...uh lets go..uh")
                            e.text_dialogbox("Narrator", "You walk to Period 2 with Linnesay")
                            e.clear_actors()
                            Lin += 1
                            classp2 += 1

                    else:
                            e.add_actor(trix["default"])
                            e.text_dialogbox("Linnesay", "Go away")
                            e.text_dialogbox("Narrator", "You walk to Period 2 alone")
                            e.clear_actors()
                            classp2 += 1
                            Lin += 1



        

    #******* PERIOD 2 DAY 1********
    if classp2 > 0:
        e._current_background = classroom
        e.text_dialogbox("Narrator", "You walk into your second period class. There are 3 other people there.")
        e.add_actor(trix["default"])
        e.add_actor(boy["default"])
        e.add_actor(ste["default"])
        e.text_dialogbox("Narrator", "You see Linnesay, Duncan, and someone you've never met before. They're looking very... unique.")
        e.clear_actors()
        e.add_actor(bono["default"])
        e.text_dialogbox("Narrator", "Your period 2 teacher walks in. His name is Mr. Albono.")
        e.text_dialogbox("Mr. Albono", "Yo yo yo, what's up some slice? You're new here right? Well let me explain how things work around here. You're gonna have to wiggity wack to the biggity back, ya hear?")
        e.text_dialogbox("Narrator", "You have no idea what just happened but you assume you need to sit down at the only desk available, at the front of the class.")
        e.text_dialogbox("Narrator", "You realize he has no idea what he's talking about because the back of the class is full of audio equipment")
        e.text_dialogbox("Mr. Albono", "Alright my cool cats and kittens, lets pick lab partners and put on safety mittens")
        e.clear_actors()
        
        input_i = e.draw_ask_dialogbox(["Linnesay", "Duncan", "New Kid"])
        if input_i == "Linnesay":
            Lin += 1
            e.add_actor(trix["default"])
            e.text_dialogbox("Narrator", "You walk up to Linnesay and ask to be partners.")
            e.text_dialogbox("Linnesay", "Ummmmm, yeah sure I guess. I mean, like, I wasn't gonna want to pair up with that doofus Duncan")
            input_i = e.draw_ask_dialogbox(["Defend Duncan", "Agree with Linnesay"])
            if input_i == "Defend Duncan":
                Dun += 1
                e.text_dialogbox("Narrator", "Linnesay seems to be upset at you, but Duncan smiles at you from across the room")
            elif input_i == "Agree with Linnesay":
                Lin += 1
                e.text_dialogbox("Linnesay", "Well it looks like we agree on something!")
                e.text_dialogbox("Narrator", "She winks at you")
            e.text_dialogbox("Narrator", "You go to the safety glove bin and grab 2 pairs.")
            e.clear_actors()
            e.add_actor(bono["default"])
            e.text_dialogbox("Mr. Albono", "Great job, you passed part 1 of the labby! Now for part 2, let's not be too shabby!")
            e.text_dialogbox("Narrator", "He goes around the class and hands each person an egg.")
            e.text_dialogbox("Mr. Albono", "This part of the class get a lil bit tricky yo! Don't drop the egg and I'll give you an A fo' sho!")
            e.clear_actors()
            e.text_dialogbox("Narrator", "He leaves the room and locks the door behind him.")
            e.add_actor(trix["default"])
            input_i = e.draw_ask_dialogbox(["Talk to Linnesay", "Throw the egg", "Make Linnesay hold egg"])
            if input_i == "Talk to Linnesay":
                Lin += 1
                e.text_dialogbox("Linnesay", "Oh hey, uhhhh, did you, like, catch that new episode of 'Trump or Stump'? It was, like, insane")
                e.clear_actors()
                e.text_dialogbox("Narrator", "All of a sudden, Mr. Albono breaks through the door")
                e.add_actor(bono["default"])
                e.text_dialogbox("Mr. Albono", "Sorry about that kids, I left my tuna salad sandwich in here. You guys can go now")
                e.text_dialogbox("Mr. Albono", "(Wait no! That didn't rhyme!) *Starts slapping self* (Stupid! Stupid! Stupid! You'll never get Sharon's respect if you can't spit mad bars!)")
                e.text_dialogbox("Narrator", "Mr. Albono gives everyone an A and starts crying at his desk. You head to your third period class")
                p3 += 1
            elif input_i == "Throw the egg":
                e.text_dialogbox("Narrator", "You prepare to throw the egg, who do you throw it at?")
                e.clear_actors()
                e.add_actor(trix["default"])
                e.add_actor(boy["default"])
                e.add_actor(ste["default"])
                p3 += 1
                input_i = e.draw_ask_dialogbox(["Linnesay", "Duncan", "New Kid"])
                if input_i == "Linnesay":
                    e.clear_actors()
                    e.add_actor(trix["default"])
                    e.text_dialogbox("Linnesay", "Ewww are you like kidding me? That's disgusting!")
                    e.clear_actors()
                    e.text_dialogbox("Narrator", "Mr. Albono bursts through the door.")
                    e.add_actor(bono["default"])
                    e.text_dialogbox("Mr. Albono", "Woah woah woah! Not cool bro! For being the new kid you sure have no flow! Grab your books and go!")
                    e.clear_actors()
                    e.text_dialogbox("Narrator", "Mr. Albono gives you an F. You should feel ashamed")
                elif input_i == "Duncan":
                    e.clear_actors()
                    e.add_actor(boy["default"])
                    e.text_dialogbox("Duncan", "Why'd you do that? I thought we were friends!")
                    e.clear_actors()
                    e.text_dialogbox("Narrator", "Mr. Albono bursts through the door.")
                    e.add_actor(bono["default"])
                    e.text_dialogbox("Mr. Albono", "Woah woah woah! Not cool bro! For being the new kid you sure have no flow! Grab your books and go!")
                    e.clear_actors()
                    e.text_dialogbox("Narrator", "Mr. Albono gives you an F. You should feel ashamed. You head to your third period class")
                elif input_i == "New Kid":
                    e.clear_actors()
                    e.add_actor(ste["default"])
                    e.text_dialogbox("Narrator", "The new kid looks at the egg as it runs all over him. He knows all that the egg has been through. He feels like him and this egg connect on a different level.")
                    e.text_dialogbox("Stevey", "I feel your pain, egg")
                    e.text_dialogbox("Narrator", "Stevey weeps silently")
                    e.clear_actors()
                    e.text_dialogbox("Narrator", "Mr. Albono bursts through the door.")
                    e.add_actor(bono["default"])
                    e.text_dialogbox("Mr. Albono", "Woah woah woah! Not cool bro! For being the new kid you sure have no flow! Grab your books and go!")
                    e.clear_actors()
                    e.text_dialogbox("Narrator", "Mr. Albono gives you an F. You should feel ashamed")
            elif input_i == "Make Linnesay hold egg":
                e.add_actor(trix["default"])
                e.text_dialogbox("Linnesay", "Ew you want me to like hold this egg for you? Uhhhhhh no way!")
                e.text_dialogbox("Narrator", "Linnesay drops both of the eggs.")
                e.clear_actors()
                e.text_dialogbox("Narrator", "Mr. Albono bursts through the door.")
                e.add_actor(bono["default"])
                e.text_dialogbox("Mr. Albono", "Woah woah woah! Not cool bro! For being the new kid you sure have no flow! Grab your books and go!")
                e.clear_actors()
                e.text_dialogbox("Narrator", "Mr. Albono gives you an F. You should feel ashamed. You head to your third period class")
            e.clear_actors()
            p3 += 1
        elif input_i == "Duncan":
            Dun += 1
            p3 += 1
            e.add_actor(boy["default"])
            e.text_dialogbox("Narrator", "You walk up to Duncan and ask to be partners.")
            e.text_dialogbox("Duncan", "Oh yeah! I'd love to be your partner! Let's go!")
            e.text_dialogbox("Duncan", "And might I just say that you're looking stunning today?")
            input_i = e.draw_ask_dialogbox(["Thank you!", "Thank... you?"])
            
            if input_i == "Thank you!":
                Dun += 1
                e.text_dialogbox("Narrator", "He smiles at you")
            if input_i == "Thank... you?":
                Lin += 1
                e.text_dialogbox("Narrator", "Duncan looks a little upset, but Linnesay found that very funny.")
            e.text_dialogbox("Narrator", "You go to the safety glove bin and grab 2 pairs.")
            e.clear_actors()
            e.add_actor(bono["default"])
            e.text_dialogbox("Mr. Albono", "Great job, you passed part 1 of the labby! Now for part 2, let's not be too shabby!")
            e.text_dialogbox("Narrator", "He goes around the class and hands each person an egg.")
            e.text_dialogbox("Mr. Albono", "This part of the class get a lil bit tricky yo! Don't drop the egg and I'll give you an A fo' sho!")
            e.clear_actors()
            e.text_dialogbox("Narrator", "He leaves the room and locks the door behind him.")
            e.add_actor(boy["default"])
            input_i = e.draw_ask_dialogbox(["Talk to Duncan", "Throw the egg", "Make Duncan hold egg"])
            if input_i == "Talk to Duncan":
                Dun += 1
                e.text_dialogbox("Duncan", "I'm glad you came to this school. I think you'll be a perfect fit here!")
                e.clear_actors()
                e.text_dialogbox("Narrator", "All of a sudden, Mr. Albono breaks through the door")
                e.add_actor(bono["default"])
                e.text_dialogbox("Mr. Albono", "Sorry about that kids, I left my tuna salad sandwich in here. You guys can go now")
                e.text_dialogbox("Mr. Albono", "(Wait no! That didn't rhyme!) *Starts slapping self* (Stupid! Stupid! Stupid! You'll never get Sharon's respect if you can't spit mad bars!)")
                e.text_dialogbox("Narrator", "Mr. Albono gives everyone an A and starts crying at his desk. You head to your third period class")
                p3 += 1
            elif input_i == "Throw the egg":
                e.text_dialogbox("Narrator", "You prepare to throw the egg, who do you throw it at?")
                e.clear_actors()
                e.add_actor(trix["default"])
                e.add_actor(boy["default"])
                e.add_actor(ste["default"])
                input_i = e.draw_ask_dialogbox(["Linnesay", "Duncan", "New Kid"])
                p3 += 1
                if input_i == "Linnesay":
                    e.clear_actors()
                    e.add_actor(trix["default"])
                    e.text_dialogbox("Linnesay", "Ewww are you like kidding me? That's disgusting!")
                    e.clear_actors()
                    e.text_dialogbox("Narrator", "Mr. Albono bursts through the door.")
                    e.add_actor(bono["default"])
                    e.text_dialogbox("Mr. Albono", "Woah woah woah! Not cool bro! For being the new kid you sure have no flow! Grab your books and go!")
                    e.clear_actors()
                    e.text_dialogbox("Narrator", "Mr. Albono gives you an F. You should feel ashamed")
                elif input_i == "Duncan":
                    e.clear_actors()
                    e.add_actor(boy["default"])
                    e.text_dialogbox("Duncan", "Why'd you do that? I thought we were friends!")
                    e.clear_actors()
                    e.text_dialogbox("Narrator", "Mr. Albono bursts through the door.")
                    e.add_actor(bono["default"])
                    e.text_dialogbox("Mr. Albono", "Woah woah woah! Not cool bro! For being the new kid you sure have no flow! Grab your books and go!")
                    e.clear_actors()
                    e.text_dialogbox("Narrator", "Mr. Albono gives you an F. You should feel ashamed. You head to your third period class")
                elif input_i == "New Kid":
                    e.clear_actors()
                    e.add_actor(ste["default"])
                    e.text_dialogbox("Narrator", "The new kid looks at the egg as it runs all over him. He knows all that the egg has been through. He feels like him and this egg connect on a different level.")
                    e.text_dialogbox("Stevey", "I feel your pain, egg")
                    e.text_dialogbox("Narrator", "Stevey weeps silently")
                    e.clear_actors()
                    e.text_dialogbox("Narrator", "Mr. Albono bursts through the door.")
                    e.add_actor(bono["default"])
                    e.text_dialogbox("Mr. Albono", "Woah woah woah! Not cool bro! For being the new kid you sure have no flow! Grab your books and go!")
                    e.clear_actors()
                    e.text_dialogbox("Narrator", "Mr. Albono gives you an F. You should feel ashamed")
            elif input_i == "Make Duncan hold egg":
                p3 += 1
                e.text_dialogbox("Duncan", "Want me to hold your egg? No problem! I don't think Albono will notice")
                e.text_dialogbox("Narrator", "Duncan winks at you")
                e.clear_actors()
                e.text_dialogbox("Narrator", "All of a sudden, Mr. Albono breaks through the door")
                e.add_actor(bono["default"])
                e.text_dialogbox("Mr. Albono", "Sorry about that kids, I left my tuna salad sandwich in here. You guys can go now")
                e.text_dialogbox("Mr. Albono", "(Wait no! That didn't rhyme!) *Starts slapping self* (Stupid! Stupid! Stupid! You'll never get Sharon's respect if you can't spit mad bars!)")
                e.text_dialogbox("Narrator", "Mr. Albono gives everyone an A and starts crying at his desk. You head to your third period class")

            p3 += 1
                
            e.clear_actors()
        elif input_i == "New Kid":
            Dun += 1
            e.add_actor(ste["default"])
            e.text_dialogbox("Narrator", "You walk up to the new kid and ask to be partners.")
            e.text_dialogbox("???", "Yeah sure. I got nothing better to do.")
            e.text_dialogbox("Stevey", "I'm Stevey by the way. I'm kind of the class clown, but not in a fun way. More like a depressing way.")
            input_i = e.draw_ask_dialogbox(["Try to cheer up Stevey", "Pretend like you didn't hear that"])
            
            if input_i == "Try to cheer up Stevey":
                Ste += 1
                e.text_dialogbox("Narrator", "Stevey gives a feint smile.")
                e.text_dialogbox("Stevey", "Thanks, but you don't need to cheer me up... It means a lot though.")
                p3 += 1
            elif input_i == "Pretend like you didn't hear that":
                e.text_dialogbox("Narrator", "The whole class goes silent.")
            e.text_dialogbox("Narrator", "You go to the safety glove bin and grab 2 pairs.")
            e.clear_actors()
            e.add_actor(bono["default"])
            e.text_dialogbox("Mr. Albono", "Great job, you passed part 1 of the labby! Now for part 2, let's not be too shabby!")
            e.text_dialogbox("Narrator", "He goes around the class and hands each person an egg.")
            e.text_dialogbox("Mr. Albono", "This part of the class get a lil bit tricky yo! Don't drop the egg and I'll give you an A fo' sho!")
            e.clear_actors()
            e.text_dialogbox("Narrator", "He leaves the room and locks the door behind him.")
            e.add_actor(ste["default"])
            input_i = e.draw_ask_dialogbox(["Talk to Stevey", "Throw the egg", "Make Stevey hold egg"])
            e.clear_actors
            if input_i == "Talk to Stevey":
                Ste += 1
                e.add_actor(ste["default"])
                e.text_dialogbox("Stevey", "Sorry if my attitude is kind of depressing. That's just the way I am")
                e.clear_actors()
                e.text_dialogbox("Narrator", "All of a sudden, Mr. Albono breaks through the door")
                e.add_actor(bono["default"])
                e.text_dialogbox("Mr. Albono", "Sorry about that kids, I left my tuna salad sandwich in here. You guys can go now")
                e.text_dialogbox("Mr. Albono", "(Wait no! That didn't rhyme!) *Starts slapping self* (Stupid! Stupid! Stupid! You'll never get Sharon's respect if you can't spit mad bars!)")
                e.text_dialogbox("Narrator", "Mr. Albono gives everyone an A and starts crying at his desk. You head to your third period class")
                p3 += 1
            elif input_i == "Throw the egg":
                e.text_dialogbox("Narrator", "You prepare to throw the egg, who do you throw it at?")
                e.clear_actors()
                e.add_actor(trix["default"])
                e.add_actor(boy["default"])
                e.add_actor(ste["default"])
                p3 += 1
                input_i = e.draw_ask_dialogbox(["Linnesay", "Duncan", "New Kid"])
                if input_i == "Linnesay":
                    e.clear_actors()
                    e.add_actor(trix["default"])
                    e.text_dialogbox("Linnesay", "Ewww are you like kidding me? That's disgusting!")
                    e.clear_actors()
                    e.text_dialogbox("Narrator", "Mr. Albono bursts through the door.")
                    e.add_actor(bono["default"])
                    e.text_dialogbox("Mr. Albono", "Woah woah woah! Not cool bro! For being the new kid you sure have no flow! Grab your books and go!")
                    e.clear_actors()
                    e.text_dialogbox("Narrator", "Mr. Albono gives you an F. You should feel ashamed")
                elif input_i == "Duncan":
                    e.clear_actors()
                    e.add_actor(boy["default"])
                    e.text_dialogbox("Duncan", "Why'd you do that? I thought we were friends!")
                    e.clear_actors()
                    e.text_dialogbox("Narrator", "Mr. Albono bursts through the door.")
                    e.add_actor(bono["default"])
                    e.text_dialogbox("Mr. Albono", "Woah woah woah! Not cool bro! For being the new kid you sure have no flow! Grab your books and go!")
                    e.clear_actors()
                    e.text_dialogbox("Narrator", "Mr. Albono gives you an F. You should feel ashamed. You head to your third period class")
                elif input_i == "New Kid":
                    e.clear_actors()
                    e.add_actor(ste["default"])
                    e.text_dialogbox("Narrator", "The new kid looks at the egg as it runs all over him. He knows all that the egg has been through. He feels like him and this egg connect on a different level.")
                    e.text_dialogbox("Stevey", "I feel your pain, egg")
                    e.text_dialogbox("Narrator", "Stevey weeps silently")
                    e.clear_actors()
                    e.text_dialogbox("Narrator", "Mr. Albono bursts through the door.")
                    e.add_actor(bono["default"])
                    e.text_dialogbox("Mr. Albono", "Woah woah woah! Not cool bro! For being the new kid you sure have no flow! Grab your books and go!")
                    e.clear_actors()
                    e.text_dialogbox("Narrator", "Mr. Albono gives you an F. You should feel ashamed")
            elif input_i == "Make Stevey hold egg":
                e.text_dialogbox("Stevey", "You want me to do what? ... fine")
                e.text_dialogbox("Narrator", "Stevey begrudgingly takes the egg")
                e.clear_actors()
                e.text_dialogbox("Narrator", "All of a sudden, Mr. Albono breaks through the door")
                e.add_actor(bono["default"])
                e.text_dialogbox("Mr. Albono", "Sorry about that kids, I left my tuna salad sandwich in here. You guys can go now")
                e.text_dialogbox("Mr. Albono", "(Wait no! That didn't rhyme!) *Starts slapping self* (Stupid! Stupid! Stupid! You'll never get Sharon's respect if you can't spit mad bars!)")
                e.text_dialogbox("Narrator", "Mr. Albono gives everyone an A and starts crying at his desk. You head to your third period class")
                p3 += 1

            e.clear_actors()


    #******* P3 Day 1********
            e.text_dialogbox("Narrator", "This is the final period of the day, you walk into class and see Issac , Britnay and Stevey")
            e.text_dialogbox("Narrator", "The only seat open is far from all of them. The teacher walks in and it is Mr.Veeman you have him again")
            e.add_actor(vee["mad"])
            e.text_dialogbox("Mr.Veeman", "Sit! DOWN! NOW! We will begin our history class now!")
            input_i = e.draw_ask_dialogbox(["Listen to History", "Just relax"])
            e.clear_actors()
            if input_i == "Listen to History":
                e.add_actor(vee["mad"])
                e.text_dialogbox("Mr.Veeman", "Bla BLa Bla 1978 Bla Bla before the mongolians Bla ")
                e.clear_actors()
            elif input_i == "Just relax":
                e.add_actor(vee["mad"])
                e.text_dialogbox("Mr.Veeman", "Bla BLa Bla 19??!? Bla Bla before or after the bnjmnongogogolaolsos Bla ")
                e.clear_actors()

            e.add_actor(vee["mad"])
            e.text_dialogbox("Mr.Veeman", "History POP TEST TIME on todays lesson! ")
            e.text_dialogbox("Mr.Veeman", "Question 1 ")
            e.text_dialogbox("Mr.Veeman","What year is super important and stuff in history! ")
            input_i = e.draw_ask_dialogbox(["1989","1978", "1968","look at a friends work"])
            if input_i == "1989":
                wrong += 1
            elif input_i == "1978":
                right += 1
            elif input_i == "1968":
                wrong += 1
            elif input_i == "look at a friends work":
                e.add_actor(vee["mad"])
                e.add_actor(Iss["default"])
                e.add_actor(Bri["default"])
                e.add_actor(Ste["default"])
                e.clear_actors()
                input_i = e.draw_ask_dialogbox(["Issac","Britenay", "Stevey","Mr.Veeman"])
                    
                if input_i == "Issac":
                    if Iss > 2:
                        e.add_actor(Iss["default"])
                        e.text_dialogbox("Issac", "Fine ILL help It ends with an 8")
                        input_i = e.draw_ask_dialogbox(["1989","1978", "1968"])
                        if input_i == "1989" or "1968":
                            wrong += 1
                        elif input_i == "1978":
                            right += 1
                            
                    elif Iss < 3:
                        e.add_actor(Iss["default"])
                        e.text_dialogbox("Issac", "SIR CHEATER!!")
                        wrong += 1
                        e.clear_actors()
                            
                elif input_i == "Britenay":
                    if Bri > 2:
                        e.text_dialogbox("Britenay", "Fine ILL try to help I think its prob smaller then 1980")
                        input_i = e.draw_ask_dialogbox(["1989","1978", "1968"])
                        if input_i == "1989":
                            wrong += 1
                        elif input_i == "1978":
                            right += 1
                        elif input_i == "1968":
                            wrong += 1
                            
                    elif Bri < 3:
                        e.text_dialogbox("Britenay", "SIR CHEATER!!")
                        wrong += 1
                        e.clear_actors()
                            
                elif input_i == "Stevey":
                    if Ste > 2:
                        e.text_dialogbox("Stevey", "Fine ill help it is bigger than 1970")
                        input_i = e.draw_ask_dialogbox(["1989","1978", "1968"])
                        if input_i == "1989" or "1968":
                            wrong += 1
                        elif input_i == "1978":
                            right += 1
                            
                    elif Ste < 3:
                        e.text_dialogbox("Stevey", "SIR CHEATER!!")
                        wrong += 1
                        e.clear_actors()
                            
                elif input_i == "Mr.Veeman":
                    e.text_dialogbox("Mr.VEEMAN", "YOU FAIL question 1 CHEATER")
                    wrong += 1
                    e.clear_actors()
                        

                    
            if right > 0:
                e.text_dialogbox("Mr.Veeman", "Good Job Smarty time for next question!")
                Iss += 1
                Ste += 1
                e.clear_actors()
            elif wrong > 0:
                e.text_dialogbox("Mr.Veeman", "Bad Job Dummy time for next question!")
                Bri += 1
                e.clear_actors()


            

            e.text_dialogbox("Mr.Veeman", "Did the mongolians strike before or after!")
            input_i = e.draw_ask_dialogbox(["After","Before"])
            if input_i == "After":
                e.text_dialogbox("Mr.Veeman", "WRONG FAILED QUESTION 2")
                wrong += 1
                e.clear_actors()
                
            elif input_i == "Before":
                e.text_dialogbox("Mr.Veeman", "CORRECT PASSED QUESTION 2")
                right += 1

                e.clear_actors()

            

            e.text_dialogbox("Mr.Veeman", "CLASS DISMISSED!")
            e.text_dialogbox("Narrator", "You finish your first day at school and go home and relax!")
            e.text_dialogbox("Narrator", "You think over the day")
            input_i = e.draw_ask_dialogbox(["Summary of day", "Start day 2"])
                    
                
                
    
    #******* BAD PATH DAY 2 skips most of day 1********


    elif bad == 2:
        e.text_dialogbox("Narrator", "You get ready for your second day")
        input_i = e.draw_ask_dialogbox(["Go", "Sleep"])


        if input_i == "Sleep":
            e.text_dialogbox("Narrator", "You decide to sleep away the day")
            e.text_dialogbox("Narrator", "The school calls telling you to come in but britnay calls to invite you to help steal beer")
            input_i = e.draw_ask_dialogbox(["Britnay", "School"])
                
        elif input_i == "Go":
            e.text_dialogbox("Narrator", "You decide to walk to school and when you get there start walking to P1")
                




            
#****Restarting Tutorial/ No paths after this part****
                
    elif input_q == "Tutorial again":
        e.text_dialogbox("", "Ok Here is how you play")
