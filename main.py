import pygame
import sys


class Ship(pygame.sprite.Sprite):

    def __init__(self, groups):
        # init parent class
        super().__init__(groups)
        # surface
        self.image = pygame.image.load('./graphics/ship.png').convert_alpha()
        # rect
        self.rect = self.image.get_rect(
            center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT/2))
        self.can_shoot = True
        self.shoot_time = None

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time > 500:
                self.can_shoot = True

    def input_position(self):
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

    def laser_shoot(self):
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

    def update(self):
        self.laser_timer()
        self.laser_shoot()
        self.input_position()


class Laser(pygame.sprite.Sprite):

    def __init__(self, groups, pos: tuple):
        super().__init__(groups)
        self.image = pygame.image.load('./graphics/laser.png').convert_alpha()
        self.rect = self.image.get_rect(
            midbottom=pos)


# basic setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
background_surf = pygame.image.load('./graphics/background.png').convert()
clock = pygame.time.Clock()
pygame.display.set_caption("Metor Shooter V2")
# end basic setup

# sprites groups
spaceship_group = pygame.sprite.Group()
laser_group = pygame.sprite.Group()

# sprite creation
ship = Ship(spaceship_group)
laser = Laser(laser_group, (50, 50))

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # delta time - to mantain FPS
    dt = clock.tick() / 1000
    # background
    display_surface.blit(background_surf, (0, 0))

    # update sprites
    spaceship_group.update()

    # graphics
    spaceship_group.draw(display_surface)
    laser_group.draw(display_surface)

    # draw frames
    pygame.display.update()
