import pygame

pygame.init()
win = pygame.display.set_mode((1300,800))
pygame.display.set_caption('Марио')
player = pygame.image.load('')
bg = pygame.image.load('')

x = 50
y = 50



speed = 5

clock = pygame.time.Clock()
run=True
while(run):
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed
    elif keys[pygame.K_UP]:
        y += speed
    elif keys[pygame.K_DOWN]:
        x -= speed

    win.blit(bg, (0, 0))
    win.blit(player,(50,50))
    pygame.display.update()
pygame.quit()