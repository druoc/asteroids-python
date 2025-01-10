import pygame
from constants import *
from player import Player

fps_clock = pygame.time.Clock()
dt = 0

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        for obj in updatable:
            obj.update(dt)
            
        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)
            
        dt = fps_clock.tick(60) / 1000
        pygame.display.flip()
    
if __name__ == "__main__":
    main()
    