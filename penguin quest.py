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

x = (display_width *0.0001) # initialise x and y (relative to display ) of penguin
y = (display_height * 0.75)


"""
Create the penguin:
"""
penguinPic = pygame.image.load('BasicPenguin.png')

w = 250
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
isJump = False
initial_jc = 13
JumpCount = initial_jc


exit = False

gameDisplay.fill(white)

while exit == False:
    for event in pygame.event.get(): # for every event the user inputs:
        if event.type == pygame.QUIT: # if someone clicks the red x in the corner
            exit = True #leave this loop, let them quit pygame
            
            
            
    keys = pygame.key.get_pressed()
    
    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
        
    else:
        if JumpCount >= -initial_jc:
            neg = 1
            if JumpCount < 0:
                neg = -1
            y -= (JumpCount **2) * 0.25 * neg
            JumpCount -=1
        else:
            isJump = False
            JumpCount = initial_jc
                  
        
        
    """
    Attempt at making a scrolling background - Lydia, you might want to use this:
    """
#    rel_y_bk = y_bk % bkgd.get_rect().height # modulo division of y position by height - 
#    
#    gameDisplay.blit(bkgd, (0,rel_y_bk - bkgd.get_rect().height))
#    if rel_y_bk == h:
#        gameDisplay.blit(bkgd, (0,rel_y_bk))
#    y_bk += 1
    gameDisplay.fill(white) # set the background to white
        
    penguin(x,y)
        
        
    pygame.display.update()
        
    clock.tick(60)
        
pygame.quit()
quit
        