import random
import pygame

pygame.init()


class Particle:
    RHO = 28.0
    SIGMA = 10.0
    BETA = 8.0/3.0
    ORIGIN = [640, 360, 360]
    dt = 0.004
    color = (255, 255, 255)

    def __init__(self, x, y, z, radius, surface) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius

        self.x_min = -25
        self.y_min = -25
        self.z_min = 0

        self.x_max = 25
        self.y_max = 25
        self.z_max = 50

        self.ox = self.x
        self.oy = self.y
        self.oz = self.z

        self.path = []
        # self.path.append([self.x , self.y])

        self.color = self.get_random_color()
        self.width, self.height = surface.get_size()

    def draw(self, surface):

        if len(self.path) <= 1:
            return

        for i in range(1, len(self.path)):
            pygame.draw.aaline(surface, self.color,
                               self.path[i - 1], self.path[i])

        pygame.draw.circle(surface, self.color, self.path[-1], self.radius)

        old_pos = self.convert_to_screen(self.ox, self.oz, self.x_min, self.z_min, self.x_max, self.z_max)
        new_pos = self.convert_to_screen(self.x, self.z, self.x_min, self.z_min, self.x_max, self.z_max)

        # old_pos = self.convert_to_screen(
        #      self.ox, self.oy, self.x_min, self.y_min, self.x_max, self.y_max)
        # new_pos = self.convert_to_screen(
        #      self.x, self.y, self.x_min, self.y_min, self.x_max, self.y_max)

        # pygame.draw.aaline(surface, self.color, old_pos, new_pos)



    def update(self):
        dx = (Particle.SIGMA * (self.y - self.x)) * Particle.dt
        dy = (self.x * (Particle.RHO - self.z) - self.y) * Particle.dt
        dz = ((self.x * self.y) - (Particle.BETA * self.z)) * Particle.dt

        self.ox = self.x
        self.oy = self.y
        self.oz = self.z

        self.x += dx
        self.y += dy
        self.z += dz

        # old_pos = self.convert_to_screen(
        #      self.ox, self.oy, self.x_min, self.y_min, self.x_max, self.y_max)
        new_pos = self.convert_to_screen(
             self.x, self.y, self.x_min, self.y_min, self.x_max, self.y_max)

        #old_pos = self.convert_to_screen(self.ox, self.oz, self.x_min, self.z_min, self.x_max, self.z_max)
        # new_pos = self.convert_to_screen(self.x, self.z, self.x_min, self.z_min, self.x_max, self.z_max)

        if len(self.path) < 50:
            self.path.append(new_pos)

        else:
            del self.path[0]
            self.path.append(new_pos)

    def convert_to_screen(self, x, y, x_min, y_min, x_max, y_max):
        new_x = self.width * (x - x_min) / (x_max - x_min)
        new_y = self.height * (y - y_min) / (y_max - y_min)

        return (new_x, new_y)

    def get_random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)
