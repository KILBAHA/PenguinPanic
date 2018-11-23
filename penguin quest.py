# =============================================================================
# """
# Penguin Panic!
# """
# =============================================================================

"""
Import variables
"""

import pygame
import random
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
red = (200,0,0)
bright_red = (255,0,0)
green = (0,200,0)
bright_green = (0,255,0)
blue = (0,0,200)
bright_blue = (0,0,255)

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
penguinPic = pygame.image.load('Resized Penguin.png')

w = 150
h = 150

penguinPic = pygame.transform.scale(penguinPic,(w,h))

def penguin(x,y):
    gameDisplay.blit(penguinPic,(x,y))

"""
Create the background:
"""
bkgd = pygame.image.load("shitbackground.jpg")

bkgd = pygame.transform.scale(bkgd,(800,600))
y_bk = 0 


def create_enemy(enemy_x, enemy_y, enemy_w, enemy_h, colour):
    pygame.draw.rect(gameDisplay, colour, [enemy_x, enemy_y, enemy_w, enemy_h])


"""
For printing text to screen - stole from tutorial, not sure how works
"""

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


"""
Special Quit game function - used for button:
"""
def quitgame():
    pygame.quit()
    quit()

"""
Function to generate buttons
"""

def button(msg,x,y,w,h,ac,ic,fn=None): # add parameter for text
    
    mouse = pygame.mouse.get_pos()
    
    click = pygame.mouse.get_pressed()
    
    if x + w > mouse[0] > x and y +h > mouse[1] > 450:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] ==1 and fn != None:
            fn()
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
    
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x + (w/2)), y + (h/2) )
    gameDisplay.blit(textSurf, textRect)


def intro_screen():
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.fill(white)
        
        largeText = pygame.font.Font ('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects("Penguin Panic!", largeText)
        TextRect.center = ((display_width * 0.5),(display_height * 0.5))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("Play",150,450,150,50,green,bright_green,game_loop) # x,y,w,h,ac,ic,fn
        
        button("Quit",550,450,150,50,red,bright_red,quitgame)
        
        button("Instructions",350, 520, 150, 50, blue, bright_blue)
        
        pygame.display.update()
        clock.tick(15)




"""
Create the gameloop:
"""

def game_loop():

    """
    Initialise variables:
    """

    x = (display_width *0.0001) # initialise x and y (relative to display ) of penguin
    y = (display_height * 0.75)
    
    
    isJump = False
    initial_jc = 13
    JumpCount = initial_jc
    
    enemy_startx = display_width
    enemy_x = enemy_startx
    enemy_starty = 490
    enemy_speed = 12
    enemy_width = 100
    enemy_height = 100
    
    dodged = 0


    exit = False
    
    """
    Main Loop:
    """
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
            
        create_enemy(enemy_x, enemy_starty, enemy_width, enemy_height, blue)
        
        enemy_x -= enemy_speed
        
        penguin(x,y)
        
        if enemy_x > x and enemy_x < x + w:
            #print("xcheck")
            if y > enemy_starty or y > enemy_starty + enemy_height and y + h > enemy_starty or y + h > enemy_starty + enemy_height:
                print("crash")
                pass
        
        if enemy_x < -enemy_width:
            dodged = dodged + 1
            print ("dodged {}".format(dodged))
            enemy_x = enemy_startx
            
            
        pygame.display.update()
            
        clock.tick(10)

intro_screen()

game_loop()
        
pygame.quit()
quit
        