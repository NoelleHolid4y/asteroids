import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
bullets = pygame.sprite.Group()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
timer = pygame.time.Clock()
dt = 0 #dt means delta time. NOT deltarune (unless...)

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (bullets, updatable, drawable)

spaceship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
asteroidBelt = AsteroidField()

def main():
    pygame.init()

def drawingScreen():
    while True:
        dt = timer.tick(60) / 1000

        screen.fill((0,0,0)) #black
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides(spaceship):
                print("Game Over!")
                raise SystemExit()
            
            for bullet in bullets:
                if bullet.collides(asteroid):
                    bullet.kill()
                    asteroid.split()
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

        for event in pygame.event.get(): #quitting game
            if event.type == pygame.QUIT:
                return
        

if __name__ == "__main__":
    main()
    drawingScreen()
