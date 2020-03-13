import pygame
import config
from elements import actor
 
pygame.init()

screen = pygame.display.set_mode(config.SCREEN_SIZE)
 
pygame.display.set_caption("Dating Simulator")


done = False

clock = pygame.time.Clock()

all_sprites_list = pygame.sprite.Group()

#f = pygame.image.load("p.png").convert()



mainAct = actor.Actor((config.SCREEN_SIZE[0]//2,config.SCREEN_SIZE[1]//2), 2, ["p.png"])

all_sprites_list.add(mainAct)

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0,25,0))

    all_sprites_list.draw(screen)
    MOUSE = pygame.mouse.get_pos()
    if mainAct.inRange([MOUSE[0], MOUSE[1]]) and pygame.mouse.get_pressed:
        print("WORKING!!!!")

    pygame.display.flip()
    
    clock.tick(60)
 

pygame.quit()
