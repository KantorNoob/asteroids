import random

from logger import log_event
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()  # Remove the current asteroid
        if self.radius <=  ASTEROID_MIN_RADIUS:
            return  # Do not split if the asteroid is too small
        log_event("asteroid_split")
        angle = random.uniform(20, 50)  # Random angle for the new asteroids
        vector_one = self.velocity.rotate(angle)
        vector_two = self.velocity.rotate(-angle)
        new_radius = self.radius / 2
        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_one.velocity = vector_one * 1.2
        asteroid_two.velocity = vector_two * 1.2