import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt):
        self.position = (self.velocity * dt) + self.position
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            first_angle = random.uniform(20, 50)
            new_vector = self.velocity.rotate(first_angle)
            opposite_vector = self.velocity.rotate(-first_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = new_vector * 1.2
            new_asteroid_2.velocity = opposite_vector * 1.2


