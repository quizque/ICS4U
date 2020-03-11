import pygame

pygame.init()

screen = pygame.display.set_mode((700, 500))

pygame.display.set_caption("Loopy Lab")

done = False

# Draw only once
drawOnce = False

# pygame clock
clock = pygame.time.Clock()

# pygame spacing
SQUARE_SPACING = 2

# draw loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # draw once
    if not drawOnce:
        drawOnce = True

        # draw grid
        for y in range(0, 500, SQUARE_SPACING*2):
            for x in range(0, 700, SQUARE_SPACING*2):
                pygame.draw.rect(screen, (255, 255, 0), (x, y, SQUARE_SPACING, SQUARE_SPACING))

        pygame.display.flip()

    clock.tick(60)
