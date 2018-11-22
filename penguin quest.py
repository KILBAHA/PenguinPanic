# =============================================================================
# """
# Penguin Game
# """
# =============================================================================

"""
Import variables
"""

import pygame

"""
Initiate Pygame
"""

pygame.init()

"""
Set Window Size and caption:
"""

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Penguin Quest')


"""
Colour Definitions
"""
black = (0,0,0) # takes RGB params
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

"""
Define Clock:
"""
clock = pygame.time.Clock()

"""
Initialise variables:
"""

x = (display_width *0.5)
y = (display_height * 0.6)


x_change = 0 # initialise x_change - we need this to move left/right

"""
Create the penguin:
"""
penguinPic = pygame.image.load('shitpenguin.png')

w = 100
h = 250

penguinPic = pygame.transform.scale(penguinPic,(w,h))

def penguin(x,y):
    gameDisplay.blit(penguinPic,(x,y))

"""
Create the background:
"""
bkgd = pygame.image.load("shitbackground.jpg")

bkgd = pygame.transform.scale(bkgd,(800,600))
y_bk = 0 

"""
Create the gameloop:
"""
exit = False


while exit == False:
    for event in pygame.event.get(): # for every event the user inputs:
        if event.type == pygame.QUIT: # if someone clicks the red x in the corner
            exit = True #leave this loop, let them quit pygame
    
        if event.type == pygame.KEYDOWN: # if they press a key down
            if event.key == pygame.K_LEFT: # if that key was the left key
                x_change = -5 # change x_change by -5
            elif event.key == pygame.K_RIGHT: # if that key was the right key
                x_change = +5 # change x_change by +5
                
                
        if event.type == pygame.KEYUP: # if they release a key
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: # if its the right/left key
                x_change = 0 # x_change becomes 0
                
    x += x_change # x_coordinate of penguin changes by x_change
        
    """
    Start drawing to the window
    """
    rel_y_bk = y_bk % bkgd.get_rect().height # modulo division of y position by height - 
    
    gameDisplay.blit(bkgd, (0,rel_y_bk - bkgd.get_rect().height))
    if rel_y_bk == h:
        gameDisplay.blit(bkgd, (0,rel_y_bk))
    y_bk += 1
    #gameDisplay.fill(white) # set the background to white
        
    penguin(x,y)
        
        
    pygame.display.update()
        
    clock.tick(60)
        
pygame.quit()
quit
        