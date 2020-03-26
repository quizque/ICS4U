#********************************************************************************
#** Nick Coombe - March 09, 2020 ***
#** Lab 5 Create-a-Picture ***
#** ***
#** Draws a cityscape with random stars in the background. ***
#** Road is drawn is polygons
#** ***
#********************************************************************************

import pygame
import random
 
pygame.init()

screen = pygame.display.set_mode((700, 500))
 
pygame.display.set_caption("Retro")

# Is program finished?
done = False

# Internal clock
clock = pygame.time.Clock()

# Draw everything once to save CPU time
drawn_once = False

###
### COLOR CONSTANTS
###

BUILDINGS_ONE_COLOR   = (12, 5, 36)
BUILDINGS_TWO_COLOR   = (25, 12, 58)
BUILDINGS_THREE_COLOR = (58, 37, 80)
BUILDINGS_FOUR_COLOR  = (141, 76, 106)

BACKGROUND_BOTTOM_COLOR = (254, 190, 162)
BACKGROUND_TOP_COLOR    = (170, 147, 203)

SUN_COLOR = (255, 255, 255)

STAR_COLOR = (218, 211, 222)

GRASS_CLOSE_COLOR = (30, 88, 107)
GRASS_FAR_COLOR   = (24, 70, 85)

ROAD_COLOR        = (59, 62, 68)
ROAD_STRIPS_COLOR = (255, 255, 255)

LIGHT_ONE_COLOR   = (200, 141, 182)
LIGHT_TWO_COLOR   = (110, 110, 184)
LIGHT_THREE_COLOR = (24, 67, 80)


# Calculate the mix of two colors
# INPUTS
#   - Color One (list)
#   - Color Two (list)
#   - Percent (float)
# OUTPUT
#   - Color (list)
def MixColor(Color1, Color2, percent):
    r = (Color1[0]-Color2[0])*percent + Color2[0]
    g = (Color1[1]-Color2[1])*percent + Color2[1]
    b = (Color1[2]-Color2[2])*percent + Color2[2]
    return (int(r),int(g),int(b))
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    
    if not drawn_once:
        drawn_once = True

        # GRADIENT DRAW BACKGROUND
        for y in range(0, 250, 1):
            pygame.draw.rect(screen, MixColor(BACKGROUND_BOTTOM_COLOR, BACKGROUND_TOP_COLOR, (1/250)*y), (0,y,700,5))

        # DRAW STARS
        for y in range(0,35):
            pygame.draw.circle(screen, STAR_COLOR, (random.randint(0,750), random.randint(0,250)), 2)

        ##
        ## SUN
        ##

        pygame.draw.circle(screen, SUN_COLOR, (225, 125), 45)

        ###
        ### BUILDINGS
        ###

        pygame.draw.rect(screen, BUILDINGS_FOUR_COLOR, (5, 150, 125, 195))
        pygame.draw.rect(screen, BUILDINGS_FOUR_COLOR, (285, 100, 115, 500))
        pygame.draw.rect(screen, BUILDINGS_FOUR_COLOR, (420, 200, 90, 175))
        pygame.draw.rect(screen, BUILDINGS_FOUR_COLOR, (575, 115, 150, 225))

        pygame.draw.rect(screen, BUILDINGS_THREE_COLOR, (0, 225, 100, 195))
        pygame.draw.rect(screen, BUILDINGS_THREE_COLOR, (325, 125, 115, 500))
        pygame.draw.rect(screen, BUILDINGS_THREE_COLOR, (210, 185, 90, 175))
        pygame.draw.rect(screen, BUILDINGS_THREE_COLOR, (500, 140, 150, 225))

        pygame.draw.rect(screen, BUILDINGS_TWO_COLOR, (50, 200, 100, 195))
        pygame.draw.rect(screen, BUILDINGS_TWO_COLOR, (300, 250, 115, 150))
        pygame.draw.rect(screen, BUILDINGS_TWO_COLOR, (200, 300, 90, 175))
        pygame.draw.rect(screen, BUILDINGS_TWO_COLOR, (600, 150, 150, 225))

        pygame.draw.rect(screen, BUILDINGS_ONE_COLOR, (10, 180, 100, 195))
        pygame.draw.rect(screen, BUILDINGS_ONE_COLOR, (125, 225, 115, 150))
        pygame.draw.rect(screen, BUILDINGS_ONE_COLOR, (290, 200, 90, 175))
        pygame.draw.rect(screen, BUILDINGS_ONE_COLOR, (475, 175, 150, 225))

        ###
        ### LIGHTS
        ###

        pygame.draw.rect(screen, LIGHT_ONE_COLOR, (20, 195, 4, 8))
        pygame.draw.rect(screen, LIGHT_ONE_COLOR, (30, 195, 4, 8))
        pygame.draw.rect(screen, LIGHT_ONE_COLOR, (20, 210, 4, 8))
        pygame.draw.rect(screen, LIGHT_ONE_COLOR, (50, 210, 4, 8))

        pygame.draw.rect(screen, LIGHT_TWO_COLOR, (150, 275, 4, 8))
        pygame.draw.rect(screen, LIGHT_TWO_COLOR, (160, 275, 4, 8))
        pygame.draw.rect(screen, LIGHT_TWO_COLOR, (170, 255, 4, 8))
        pygame.draw.rect(screen, LIGHT_TWO_COLOR, (190, 255, 4, 8))

        pygame.draw.rect(screen, LIGHT_THREE_COLOR, (300, 225, 4, 8))
        pygame.draw.rect(screen, LIGHT_THREE_COLOR, (325, 275, 4, 8))
        pygame.draw.rect(screen, LIGHT_THREE_COLOR, (325, 255, 4, 8))
        pygame.draw.rect(screen, LIGHT_THREE_COLOR, (300, 255, 4, 8))


         # GRADIENT DRAW GRASS
        for y in range(375, 500, 1):
            pygame.draw.rect(screen, MixColor(GRASS_CLOSE_COLOR, GRASS_FAR_COLOR, (1/125)*(y-375)), (0,y,700,5))

        ##
        ## ROAD
        ##

        pygame.draw.polygon(screen, ROAD_COLOR, ((400,375), (300,375), (100,500), (600,500)))

        pygame.draw.polygon(screen, ROAD_STRIPS_COLOR, ((395,375), (392,375), (585,500), (595,500)))
        pygame.draw.polygon(screen, ROAD_STRIPS_COLOR, ((305,375), (308,375), (115,500), (105,500)))

        pygame.draw.polygon(screen, ROAD_STRIPS_COLOR, ((365, 500), (335, 500), (345, 425), (355, 425)))

        pygame.draw.polygon(screen, ROAD_STRIPS_COLOR, ((349, 380), (351, 380), (352, 400), (347, 400)))
        
        pygame.display.flip()

    clock.tick(60)

pygame.quit()