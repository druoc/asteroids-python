import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
            pygame.draw.circle(screen, 'red', self.position, self.radius, width=2)
            
    def update(self, dt):
            self.position += self.velocity * dt
            
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_angle = random.uniform(20, 50)
        vector_a = self.velocity.rotate(new_angle)
        vector_b = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = vector_a * 1.3
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = vector_b * 1.3
            
            
            

