import os
from random import choice
import pygame

pygame.init()
bg = pygame.image.load('bg.png')
screen = pygame.display.set_mode((bg.get_width(), bg.get_height()))
pygame.display.set_caption('Марио')


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Wall(pygame.sprite.Sprite):
    items = ['wall.png', 'mushroom.png', 'tube.png', 'angry mushroom.png', 'tree.png']
    pictures = []
    for item in items:
        image = load_image(item)
        res_image = pygame.transform.scale(image, (60, 60))
        pictures.append(res_image)
    wall_image = choice(pictures)

    def __init__(self, group):
        super().__init__(group)
        self.image = Wall.wall_image
        self.rect = self.wall_image.get_rect()
        self.rect.x = 1024
        self.rect.y = 390
        self.mask = pygame.mask.from_surface(self.wall_image)

    def update(self, xspeed):
        self.rect.x -= xspeed

    def change_image_and_pos(self):
        items = ['wall.png', 'mushroom.png', 'tube.png', 'angry mushroom.png', 'tree.png']
        pictures = []
        for item in items:
            image = load_image(item)
            res_image = pygame.transform.scale(image, (60, 60))
            pictures.append(res_image)
        self.image = choice(pictures)
        self.rect.x = 1024


if __name__ == '__main__':
    players = pygame.sprite.Group()
    player = pygame.sprite.Sprite()
    player_image = load_image('sprite.png')
    player.image = pygame.transform.scale(player_image, (50, 70))
    player.rect = player.image.get_rect()
    players.add(player)
    player.rect.x = 50
    player.rect.y = 380

   # Wall(all_wall_sprites)

    y = 380

    speed = 4
    is_jump = False
    yspeed = 0
    xspeed = 5
    score = 0

    clock = pygame.time.Clock()

    all_wall_sprites = pygame.sprite.Group()
    wall = Wall(all_wall_sprites)

    run = True
    while run:
        clock.tick(50)
        score += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if is_jump:
            y -= yspeed
            yspeed -= 1
        elif keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            is_jump = True
            yspeed = 17
        if y > 380:
            is_jump = False
            yspeed = 0
            y = 380
        if score >= 500:
            xspeed = 7
            if score >= 1000:
                xspeed = 10

        screen.blit(bg, (0, 0))
        players.draw(screen)
        all_wall_sprites.draw(screen)
        player.rect.y = y
        all_wall_sprites.update(xspeed)
        pygame.display.update()
        if wall.rect.x <= 0:
            wall.change_image_and_pos()
        if player.rect.x > bg.get_width():
            player.rect.x = 0
    pygame.quit()

