import pygame
import random
 
pygame.init()

screen = pygame.display.set_mode((700, 500))
 
pygame.display.set_caption("Example")

# Is program finished?
done = False

# Internal clock
clock = pygame.time.Clock()
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit() ########### Suppose to quit game?

################## Then this shouldn't run down here but it does.....
for i in range(25):
    print("Still running....")