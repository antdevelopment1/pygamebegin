import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (250, 100), 50, 0)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
