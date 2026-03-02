import sys
import pygame
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    pygame_ver = pygame.version.ver
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame_ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt) 
        for obj in drawable:
            obj.draw(screen)
        for object in asteroids:
            if object.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if bullet.collides_with(object):
                    log_event("asteroid_shot")
                    object.split()
                    bullet.kill()
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()
