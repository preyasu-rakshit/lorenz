import random
import sys
import pygame
from particle2 import Particle

pygame.init()

screen_size = (1280, 720)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Lorenz Atrractor")
clock = pygame.time.Clock()

particles = []
for i in range(100):
    x = random.uniform(0.1, 2)
    y = random.uniform(0.1, 2)
    z = random.uniform(24, 25)
    particles.append(Particle(x, y, z, 3, screen))


def make_video(screen):
    _image_num = 0
    while True:
        _image_num += 1
        str_num = "000" + str(_image_num)
        file_name = "image" + str_num[-4:] + ".png"
        pygame.image.save(screen, 'video\ '.rstrip(' ') + file_name)
        yield


save_screen = make_video(screen)
video = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_v:
                video = not video

    screen.fill([0, 0, 0])

    for particle in particles:
        particle.draw(screen)
        particle.update()

    # print(clock.get_fps())
    if video:
        next(save_screen)
    pygame.display.flip()
    clock.tick(100)