import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from logger import log_event
import sys
from shot import Shot

def main():
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  


    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while 1 + 1 == 2:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)
        for obj in updatable:
            if obj == player:
                player.shot_cooldown -= dt
                player.update(dt)
            else:
                obj.update(dt)

        for obj in asteroids:
            for bang in shots:
                if obj.collides_with(bang):
                    log_event("asteroid_shot")
                    bang.kill()
                    new_asteroids = obj.split()
                    if new_asteroids:
                        for a in new_asteroids:
                            asteroids.add(a)
        

        for obj in asteroids:
            if obj.collides_with(player):
                log_event("player_hit")
                print("Game over!") 
                sys.exit()

        pygame.display.flip()
        
        clock.tick(60)
        time_elapsed = clock.tick(60)
        dt = time_elapsed / 1000

       


if __name__ == "__main__":
    main()
