import pygame
import random
import time

pygame.init() # initiates pygame

display_width = 800 # No magic numbers!!!
display_height = 600

"""
Colour Definitions - defined with RGB

"""

black = (0,0,0) # R,G,B
white = (255,255,255) # 255 is max (256 options including 0)

red = (200,0,0)
bright_red = (255,0,0)
green = (0,200,0)
bright_green = (0,255,0)
blue = (0,0,200)

carImg = pygame.image.load('shitcar.png') #loads the image - make sure is in same directory as game!

cw, ch = 150, 200

carImg = pygame.transform.scale(carImg,(ch,cw)) # scale the image to a particular height and width

gameDisplay = pygame.display.set_mode((display_width,display_height)) # set width and height (resolution), takes one parameter hence tuple

pygame.display.set_caption('A bit racey') # Set title of window

clock = pygame.time.Clock() #Define clock - times things, useful for FPS

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, red)
    gameDisplay.blit(text, (0,0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh]) # draw a rectangle to screen with xy coordinates and width and height


def car(x,y):
    gameDisplay.blit(carImg,(x,y))#write to the screen the car image at x,y. (x,y) is a tuple
    
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width * 0.5),(display_height * 0.5))
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()
    
    time.sleep(2) # will leave message on screen for two seconds, needed to import time to use this command
    
    
def crash():
    message_display('You Crashed!') # message on screen displayed
    game_loop() # start the game back up again
    
    
def button(msg,x,y,w,h,ic,ac, action=None): # message, width, height, inactive, active, action
    
    mouse = pygame.mouse.get_pos()
    
    click = pygame.mouse.get_pressed()
        
    if x + w > mouse[0] > x and y+h >mouse[1] > 450:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] ==1 and action!= None:
            action()
            
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
        
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x + (w/2)), y + (h/2) )
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()
    
def game_intro():
    
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event .type == pygame.QUIT:
                pygame.quit()
                quit()
    
        gameDisplay.fill(white)
    
        largeText = pygame.font.Font ('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width * 0.5),(display_height * 0.5))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("GO!",150,450,100,50, green,bright_green, game_loop)
        
        button("Quit",550,450,100,50, red,bright_red, quitgame)
        
        pygame.display.update()
        clock.tick(15)
    

def game_loop():    
    x = (display_width * 0.5) 
    y = (display_height * 0.75)
    
    x_change = 0
    
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100
    
    thing_count = 1
    
    dodged = 0
    
    gameExit = False 
    
    while not gameExit: # while crashed is still false
        
        for event in pygame.event.get(): # gets any event in pygame (e.g. key presses mouse movement) - creates a list of event per frame per second
            if event.type == pygame.QUIT: # If someone hits the x in the window
                gameExit = True # lets us break out of the loop!
                
            if event.type ==pygame.KEYDOWN: # if someone pressed a key
                if event.key == pygame.K_LEFT: # If that key was the left key
                     x_change = -5 # To move left we must decrease our x value
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                    
                    
            if event.type == pygame.KEYUP: #IF key has been released and moved up
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: # if the key beeing released is either left or right arrow
                    x_change = 0 # set x_change back to 0 once you've stopped pressing the button
                    
        x += x_change
        
        gameDisplay.fill(white) # change background to white - do this before you draw anything else!
        
        things(thing_startx, thing_starty, thing_width, thing_height, green)
        
        thing_starty += thing_speed
        
        car(x,y) # draw the car
        things_dodged(dodged)
        
        if x > display_width-cw or x < 0: # if you're going over the bounds of the window, object's coordinates = pixel at top left coordinate
            crash() # if you've gone off bounds, run the crash function
        
        
        if thing_starty > display_height: # if the thing moves off the screen
            thing_starty = 0 - thing_height # reset the y  of thing
            thing_startx = random.randrange(0,display_width) # reset the x of thing
            dodged += 1
            #thing_speed += 1
            thing_width += (dodged * 1.2)
        
        if y < thing_starty+thing_height: # checking for collisions
            
            if x > thing_startx and x < thing_startx + thing_width  or x + cw > thing_startx and x + cw < thing_startx + thing_width: # car colision
                crash()
            
        
        pygame.display.update() # updates surface (window). If parameter included, will just update whatever between brackets
        #pygame.display.flip() - will refresh entire surface (rather than just updates, not v useful)
        
        clock.tick(60) # dictates FPS - can speed things up by changing FPS
    pygame.quit()

game_intro()
game_loop()    
pygame.quit() # turns off pygame
quit # quits the programme