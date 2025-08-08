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
dt = 0 #delta time (deltarune reference...)

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (bullets, updatable, drawable)

spaceship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
asteroidBelt = AsteroidField()


def main():
    pygame.init()
    pygame.display.set_caption("Asteroids!")

def drawingScreen():
    score = 0.0
    terminalfont = pygame.font.SysFont("Terminal", 25)
    
    while True:
        dt = timer.tick(60) / 1000

        screen.fill((0,0,0)) #black
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides(spaceship):
                print("Game Over!")
                print("Score: " + str(score))
                raise SystemExit()
            
            for bullet in bullets:
                if bullet.collides(asteroid):
                    bullet.kill()
                    asteroid.split()
                    score += 1
        
        scoreText = terminalfont.render(f"Score: {score}", False, (255,255,255)) #False is for antialiasing
        scoreRect = scoreText.get_rect()
        scoreRect.center = ((SCREEN_WIDTH / 2, 25))
        
        for obj in drawable:
            obj.draw(screen)
        screen.blit(scoreText, scoreRect)

        pygame.display.flip()

        for event in pygame.event.get(): #quitting game
            if event.type == pygame.QUIT:
                print("Score: " + str(score))
                return
        

if __name__ == "__main__":
    main()
    drawingScreen()
