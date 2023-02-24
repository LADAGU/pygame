import pygame

pygame.init()
win = pygame.display.set_mode((1024, 576))
pygame.display.set_caption('Марио')
player = pygame.image.load('sprite.png')
bg = pygame.image.load('bg.png')

x = 50
y = 370


speed = 4
is_jump = False
yspeed = 0


clock = pygame.time.Clock()
run = True
while run:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if is_jump:
        y -= yspeed
        yspeed -= 2
    elif keys[pygame.K_UP] or keys[pygame.K_SPACE]:
        is_jump = True
        yspeed = 24
    if y > 370:
        is_jump = False
        yspeed = 0
        y = 370

    win.blit(bg, (0, 0))
    win.blit(player, (50, y))
    pygame.display.update()
pygame.quit()
