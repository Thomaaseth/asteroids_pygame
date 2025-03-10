import pygame
from constants import *
from player import Player

def main():

    pygame.init() 
    clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width:", SCREEN_WIDTH)
    print(f"Screen height:", SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)


    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     return

        screen.fill('black')
        updatable.update(dt)
        
        for drawable_object in drawable:
            drawable_object.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()
    
