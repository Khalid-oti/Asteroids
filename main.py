import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (bullets, updatables, drawables)

    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield1 = AsteroidField()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))

        for drawable in drawables:
            drawable.draw(screen)
        for updatable in updatables:
            updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collision(player1):
                print("Game over!")
                sys.exit()
            for bullet in bullets:
                if asteroid.check_collision(bullet):
                    asteroid.split()
                    bullet.kill()

        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
