import pygame

pygame.init()

screen = pygame.display.set_mode((700, 500))

pygame.display.set_caption("Loopy Lab")

done = False
drawOnce = False

clock = pygame.time.Clock()

SQUARE_SPACING = 2

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if not drawOnce:
        drawOnce = True

        for y in range(0, 500, SQUARE_SPACING*2):
            for x in range(0, 700, SQUARE_SPACING*2):
                pygame.draw.rect(screen, (255, 255, 0), (x, y, SQUARE_SPACING, SQUARE_SPACING))

        pygame.display.flip()

    clock.tick(60)