# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()

w,h = 1000, 500

screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("lightblue")

    n = 0
    while n <= w:
        pygame.draw.line(screen,"black",(n,0),(n,h),width=5)
        n += 50
    
    n = 0

    while n <= h:
        pygame.draw.line(screen,"black",(0,n),(w,n),width=5)
        n += 50



    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()












