import pygame
import os
pygame.init()


WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")

FPS = 60
VEL = 7

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        # WIN.blit()
        clock.tick(FPS)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
    pygame.quit()


if __name__ == "__main__":
    main()