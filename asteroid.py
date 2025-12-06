from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        pygame.sprite.Sprite.kill(self)

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            
            ANGLE = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            split_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            split_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            split_asteroid_one.velocity = self.velocity.rotate(ANGLE) * 1.2
            split_asteroid_two.velocity = self.velocity.rotate(-ANGLE) * 1.2
            return split_asteroid_one, split_asteroid_two



