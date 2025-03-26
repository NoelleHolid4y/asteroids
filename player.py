import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self,x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(
            screen, (255,255,255), self.triangle(), 2 #line width
        )
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            if self.timer < 0:
                self.shoot()
    
    def shoot(self):
        bullet = Shot(self.position.x, self.position.y)
        speedVector = pygame.math.Vector2(0,1)
        speedVector = speedVector.rotate(self.rotation)
        bullet.velocity = speedVector * BULLET_SPEED

        self.timer = BULLET_COOLDOWN


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, BULLET_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 4)
    
    def update(self, dt):
        self.position += self.velocity * dt
    