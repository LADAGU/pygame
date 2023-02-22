import pygame

pygame.init()
win = pygame.display.set_mode((1024, 576))
pygame.display.set_caption('Марио')
player = pygame.image.load('sprite.png')
bg = pygame.image.load('bg.png')

x = 50
y = 370


speed = 4
yupst = 200
yup = 200


clock = pygame.time.Clock()
run = True
while run:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if y <  yup and yup < 370:
        y += speed
        yup += speed
    elif yup >= 370:
        yup = yupst
    elif keys[pygame.K_UP] or keys[pygame.K_SPACE]:
        y -= speed
    elif y < 370:
        y += speed

    win.blit(bg, (0, 0))
    win.blit(player, (50, y))
    pygame.display.update()
pygame.quit()
