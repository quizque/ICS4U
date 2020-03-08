import pygame
 
pygame.init()

screen = pygame.display.set_mode((700, 500))
 
pygame.display.set_caption("Retro")
 
done = False
clock = pygame.time.Clock()

drawn_once = False

BUILDINGS_ONE_COLOR   = (12, 5, 36)
BUILDINGS_TWO_COLOR   = (25, 12, 58)
BUILDINGS_THREE_COLOR = (58, 37, 80)
BUILDINGS_FOUR_COLOR  = (141, 76, 106)

BACKGROUND_BOTTOM_COLOR = (254, 190, 162)
BACKGROUND_TOP_COLOR    = (170, 147, 203)

SUN_COLOR = (255, 255, 255)

GRASS_CLOSE_COLOR = (30, 88, 107)
GRASS_FAR_COLOR   = (24, 70, 85)

ROAD_COLOR        = (59, 62, 68)
ROAD_STRIPS_COLOR = (255, 255, 255)

LIGHT_ONE_COLOR   = (200, 141, 182)
LIGHT_TWO_COLOR   = (110, 110, 184)
LIGHT_THREE_COLOR = (24, 67, 80)

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

        # GRADIENT DRAW GRASS
        for y in range(375, 500, 1):
            pygame.draw.rect(screen, MixColor(GRASS_CLOSE_COLOR, GRASS_FAR_COLOR, (1/125)*(y-375)), (0,y,700,5))

        pygame.draw.polygon(screen, ROAD_COLOR, ((400,375), (300,375), (100,500), (600,500)))
        pygame.draw.polygon(screen, ROAD_STRIPS_COLOR, ((395,375), (392,375), (585,500), (595,500)))
        pygame.draw.polygon(screen, ROAD_STRIPS_COLOR, ((305,375), (308,375), (115,500), (105,500)))
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()