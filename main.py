"""
A note on references:
    
    have used footnotes $N$ that refer to references.txt where N = reference No
"""
#Import modules:
import pygame
import time
import random
import math

from pp_variables import * # calls the file where we stored variables outside of the game loop

import os # to make the game MacOS compatable 


#Initiate pygame:
pygame.init()
#Initiate the pygame mixer:
pygame.mixer.init()


"""
Define Classes for OOP
"""

class Background(): 
    """
    $1$
    """
    
    bkgd = pygame.image.load("bg2.jpg").convert() #load background image $2$
    x = 0 # initial x
    
    def Scroll(self):
        rel_x = self.x % self.bkgd.get_rect().width # calculate rel_x - % of background width
        gameDisplay.blit(self.bkgd,(rel_x - self.bkgd.get_rect().width, 0)) #blit background to rel_x minus width of background
        
        #when rel_x < display_width, print the background along y= 0
        if rel_x < display_width: 
            gameDisplay.blit(self.bkgd,(rel_x,0)) # gets rid of tear
        
        self.x -=1 # decrease the x co-ordinate (leads to scroll)


class Penguin():
    
    penguinPic = pygame.image.load('Sliding Penguin.png') # variable for penguin sprite
    
    w = 130
    h = 80 # used for transformation

    penguinPic = pygame.transform.scale(penguinPic,(w,h)) #transform penguin sprite to w,h
    
    width = penguinPic.get_rect().width 
    height = penguinPic.get_rect().height
    """
    $3$
    """
    isJump = False # variable used for "jump"
    initial_jc = 16 # use to change size of jump
    JumpCount = initial_jc # This variable changes as Jump is executed
    jump_lim = 0.2 # increase to increase jump height + jump acceleration/deceleration
    keys = pygame.key.get_pressed() #Allows registering of user input
    lives = 5 # players lives
    
    x = (display_width *0.0001) # initialise x and y (relative to display ) of penguin
    y = (display_height - (height-3))
    startx = x 
    starty = y # reference to original x and y
    vx = 15 # speed for horizontal movement
        
    def __init__(self,x,y): # initialisation of objects includes x and y
        self.x = x
        self.y = y
    
    def move(self,iput): # function to move penguin
        if iput == "L": # if player wants to move left
            if self.x > self.vx: # and is not already beyond x=0
                self.x -= self.vx # decrease x co-ordinate by vx
        if iput == "R":
            if self.x < display_width - self.width: #if player's x not greater than screen width - length of sprite
                self.x += self.vx # increase co-ordinate by vx


    
    def reset(self): # used during collision 
        self.isJump = False # player not still jumping after colision
        self.JumpCount = self.initial_jc # jump count is reset
        self.x = self.startx # player x reset
        self.y = self.starty # player y reset
        
    def display(self,x,y): # used to blit penguin to screen
        gameDisplay.blit(self.penguinPic,(x,y))
    
    def Life_Count(self): # displays lives in top left
        font = pygame.font.SysFont(None, 25)
        text = font.render("Lives x{}".format(self.lives), True, black)
        gameDisplay.blit(text, (0,0))
        
    def jump(self):
        """
        $3$
        """
        if self.isJump: # if jump == true
                if self.JumpCount >= -self.initial_jc: # if JC > negative original JC
                    neg = 1 # set this to negative value for negative values of JC
                    if self.JumpCount < 0:
                        neg = -1 # set this to negative value for negative values of JC
                    self.y -=(self.JumpCount**2)*self.jump_lim*neg # creates a quadratic curve for difference in y
                    self.JumpCount -= 1 # decrease the jump count by one
                else: # runs after the jump
                    self.isJump = False # reset Jump to false
                    self.JumpCount = self.initial_jc # reset the jump count

class Rock():
    
    rockPic = pygame.image.load("rock.png") # load rock sprite
    w = 30
    h = 30 # used for transformation 
    rockPic = pygame.transform.scale(rockPic,(w,h)) # transform rock to w,h
    speed = 15 # horizontal speed of rock
    projectiles = [] # empty list for rocks - allows > 1 to exist on screen
    
    def create_rock(): # function to create rocks
        """
        $4$
        """
        
        global rock_count
        keys = pygame.key.get_pressed()        
        
        if keys[pygame.K_UP]: # if you press up, append list to contain rock object
            if len(Rock.projectiles) < 3: #set this to 3
                if rock_count >= 5: # rock_count - used to create short delay between throwing rocks
                    Rock.projectiles.append(Rock(player.x +75, player.y +75, 100, 13))
                    rock_count = 0 # reset rock count 
             
    def resetrocks(self): # delete every rock on screen when called
        for projectile in self.projectiles:
            self.projectiles.pop(self.projectiles.index(projectile))
            
    def __init__(self,x,y,itc,tc): # create rocks with penguins x, y, and set itc and tc
        self.x = x
        self.y = y
        self.itc = itc #initial throw count
        self.tc = tc # throw count
    
    def checkRock(self): # check off screen
        for projectile in self.projectiles:
            if projectile.x > display_width and projectile.y > display_height: # if it's offscreen, delete
                self.projectiles.pop(self.projectiles.index(projectile))
    
    def move_draw_check(self): # similar to jump function (see above)
        self.x += self.speed
        if self.tc >= -self.itc:
            neg = 1
            if self.tc < 0:
                neg = -1
            self.y -= (self.tc ** 2) * 0.4*neg
            self.tc -= 1
        gameDisplay.blit(self.rockPic,(self.x,self.y))
        self.checkRock() # check to see if off screen
       
       
class Enemy():
    lives = 10 # Enemy lives set to 10
    startx = display_width # set enemy start_x to edge of screen
    
    def reset_x(self): # will reset x co-ordinate of enemy after colision, is randomised 
        self.x = self.startx + random.randint(100, 400)
        
    def checkoffscreen(self):    
        if self.x <- self.width:
            self.reset_x() # call reset x when enemy moves offscreen
            
    def reset_all(self): # function to reset all objects 
        my_bird.reset_x()
        my_seal.reset_x()
        slow_seal.reset_x()
        slow_bird.reset_x()
        for barrel in Barrel.barrels:
            Barrel.barrels.pop(Barrel.barrels.index(barrel))

#can we bundle


    def checkrockcollision(self): # check if collision between enemy + rock
        global projectiles
        for projectile in Rock.projectiles:
            if self.x < projectile.x and self.x + self.width > projectile.x + projectile.w:
                if projectile.y > self.y and self.y + self.width > projectile.y + projectile.h:
                    self.lives -=1 # decrease enemy lives by one
                    Rock.resetrocks(Rock) # reset the rock that hit the enemy
                    self.reset_x()    # reset the enemy x co-ordinate
                    rocksound.play() # play rocksound

    def checkcolision(self):
        """
        $5$
        """
        
        if self.x < player.x + player.width and self.x > player.x or self.x + self.width < player.x + player.width and self.x + self.width > player.x: # check x co-ordinate
            if self.y > player.y and self.y < player.y + player.height or self.y + self.height > player.y and self.y + self.height < player.y + player.height: # check y co-ordinate
                player.lives -= 1 # decrease player life
                livedown.play() # sound effect for life down
                self.reset_all() # reset all enemies location
                player.reset() # reset player location 
                for projectile in Rock.projectiles: 
                    Rock.resetrocks(Rock) # reset all rocks
                Death() # print death message
                    
                    
    
    def move_draw_check(self): 
        global BOSS
        if self.lives > 0: # only draw to screen when enemy life is greater than 0
            self.x -= self.speed # move enemy in x direction by speed
            self.y += self.vy # move enemy in y direction by vy
            if self.y <= 0: # if enemy's y is at top of screen:
                self.vy = -self.vy # reverse direction of velocity
            if self.y >= display_height - 300: # if enemy moves > 300 pixels below screen top
                self.vy = -self.vy # reverse velocity
            self.draw() # draw enemy
            self.checkcolision() # check for enemy colision 
            self.checkoffscreen() # check if enemy off screen
            self.checkrockcollision() # check for rock collision with enemy
        else:
            bossmessage() # run boss message
            BOSS = True # set BOSS to true

class Barrel(Enemy): 
    width = 68
    height = 68
    barrelPic = pygame.image.load("Oil Barrel.png") # load image
    barrelPic = pygame.transform.scale(barrelPic,(width,height)) # scale to width and height
    vel = 15 # speed barrel moves 
    barrels = [] #empty list for projectiles
    
    def __init__(self, x, y): #tx and ty are target x and target y, to allow it to be thrown at the player
        """
        $6$
        """            
        self.x = x
        self.y = y
        self.tx = player.x
        self.ty = player.y
        self.startx = x
        self.starty = y # start.x and start.y allow to calculate angle to be thrown at
        self.x_diff = self.tx - self.startx #calculating difference allows us to calculate angle
        self.y_diff = self.ty - self.starty
        self.angle = math.atan2(self.y_diff, self.x_diff) # uses y diff and x diff to find angle between player and boss
        self.changex = math.cos(self.angle) * self.vel 
        self.changey = math.sin(self.angle) * self.vel
    
    def draw(self):
        gameDisplay.blit(self.barrelPic,(self.x,self.y)) # blit the barrel
    
    def createBarrel(): # allows only 1 barrel on screen at a time
        if len(Barrel.barrels) < 1:
            Barrel.barrels.append(Barrel(my_boss.x + 50, my_boss.y + 50))
            
    def check_offscreen(self): # if barrel off screen, then delete
        for barrel in self.barrels:
            if barrel.x < 0 - barrel.width or barrel.y > display_height:
                self.barrels.pop(self.barrels.index(barrel))
                
            
    def move_draw_check(self): # y and x change by change x, draw to screen, check for colission/ offscreen
        self.x += self.changex
        self.y += self.changey
        self.draw()
        self.checkcolision()
        self.check_offscreen()
        #gameDisplay.blit(self.barrelPic,(self.x, self.y))

class Boss(Enemy):
    
    BossPic = pygame.image.load('bp_baloon.png') # load boss sprite
    
    w = 145
    h = 285 # used for transformation

    BossPic = pygame.transform.scale(BossPic,(w,h)) #transform boss sprite
    
    lives = 3 # boss has 3 lives
    
    def __init__(self, x, y ): # initialise with x, and y
        self.x = x
        self.y = y
        self.startx = x # create start x and y to inital x and y
        self.starty = y

    width = 100
    height = 100 # for collision code - we want the penguin to hit the balloon
    vy = 3 # vertical speed
    vx = -3 # horizontal speed
    
    
    def draw(self): # function to blit Boss and x and y
        gameDisplay.blit(self.BossPic,(self.x,self.y))
    
    
    def reset_x(self): # function to reset the x co-ordinate of boss
        self.y = 1 # set him to top of screen

    
    def move_draw_check(self):
        global epilogue
        
        self.y += self.vy
        self.x += self.vx
        
        if self.y <= 0:
            self.vy = -self.vy # if hit screen top, then reverse velocity

        if self.y >= display_height - self.h:
            self.vy = -self.vy # if hit screen bottom, reverse velocity
            
        if self.x <= display_width - 200:
            self.vx = -self.vx # causes jitter when colides with this bound
        
        if self.lives > 0: #will draw to screen only when boss has positive lives
            self.draw()
            self.checkcolision()
            self.checkoffscreen()
            self.checkrockcollision()
        else:
            epilogue = True # set epilogue to true and run epilogue screen

class Bird(Enemy):
    
    
    birdPic1 = pygame.image.load('Bird1.png') # Load bird images
    birdPic2 = pygame.image.load('Bird2.png')
    
    w = 100
    h = 100 # used for transform - not actual width and height!
    
    birdPic1 = pygame.transform.scale(birdPic1, (w,h))
    birdPic2 = pygame.transform.scale(birdPic2,(w,h)) # transform bird images
    
    width = birdPic1.get_rect().width # get width and height for collision detection
    height = birdPic1.get_rect().height
    
    starty = display_height - 400 # set start y
    y = starty
    
    vy = 4 # set vertical speed
    
    def __init__(self,x,speed): #initialise x and speed
        """
        $7$
        """
        
        self.x = x 
        self.speed = speed
        
        self.images = [] # empty list for images to be stored and recalled
        for i in range (3):
            self.images.append(self.birdPic1) # adds 3 images of pic 1 to list
        for i in range(3):
            self.images.append(self.birdPic2) # adds 3 images of pic 2 to list - added 3 to slow down transition 
        self.index = 0 #innitialised self.index (initialised to first sprite)
        self.image = self.images[self.index] # self.image is the object in images with the next index        
    
    def update(self):
        self.index += 1 # increase the index by 1 to update
        
        if self.index >= len(self.images): # reset once at end of list
            self.index = 0
            
        self.image = self.images[self.index] # set self.image to updated index
        
    def draw(self):
        gameDisplay.blit(self.image,(self.x,self.y)) # blit to x and y


class Seal(Enemy):
    
   
    sealPic = pygame.image.load('Seal.png') #Load Seal image
    
    w = 150
    h = 100 # used for transform - not actual width/height
    
    sealPic = pygame.transform.scale(sealPic,(w,h)) # transform seal image
    
    width = sealPic.get_rect().width
    height = sealPic.get_rect().height # get width and height for collision 
    
    starty = display_height - (height) # set start y co-ordinate to height of seal sprite
    vy = 0 # has no vertical velocity
    y = starty 
    
    def __init__(self, x, speed ): # initialise with x and speed
        self.x = x
        self.speed = speed
        
    def draw(self): # blit to x and y
        gameDisplay.blit(self.sealPic,(self.x,self.starty))


def quitgame(): # specialised function to quit game
    pygame.quit() # quit pygame
    os._exit(0) # for mac support
    quit() # quit python
    
"""
Function to generate buttons
"""

"""
$8$
"""

def button(msg,x,y,w,h,ac,ic,fn=None): # Function to create buttons, takes params x, y, width, height, active colour, inactive colour and a function which is set to none by default
    
    mouse = pygame.mouse.get_pos() # get mouse posission
    
    click = pygame.mouse.get_pressed() # get mouse clicks
    
    if x + w > mouse[0] > x and y +h > mouse[1] > 450: # if mouse x and y are in bounds of box
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h)) # blit a rectangle button with its active colour
        if click[0] ==1 and fn != None: # if you click while mouse is in bounds
            fn() # add () to the end of the function - causes it to run
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h)) # else draw the button in the same position with its inactive colour
    
    """
    used to display text:
    """
    
    smallText = pygame.font.Font("freesansbold.ttf", 20) 
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x + (w/2)), y + (h/2) )
    gameDisplay.blit(textSurf, textRect)

def text_objects(text, font):
    """
    $8$
    Used to display text:
    """
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    """
    $8$
    Used to display text:
    """
    in_game_font = pygame.font.Font("freesansbold.ttf", 60)
    TextSurf, TextRect = text_objects(text, in_game_font)
    TextRect.center = ((display_width * 0.5), (display_height * 0.5))
    gameDisplay.blit(TextSurf, TextRect)
    
def bossmessage():
    global already_run_message
    
    if already_run_message == False: # if haven't already run message
        message_display("Warning! Boss Incoming!") # blit message to screen 
        pygame.display.update() # update display
        time.sleep(2) # wait 2 seconds
        already_run_message = True # prevent from triggering every frame

def Death():
    for event in pygame.event.get(): # if player clicks red x, quit game
            if event.type == pygame.QUIT:
                quitgame()

    if player.lives >=2: # if players lives > 1 then display normal death message
        gameDisplay.blit(deathmessage_1,(0,0))
    elif player.lives == 1: # if player lives == 1 then display special death message
        gameDisplay.blit(deathmessage_2,(0,0))
    else:
        gameDisplay.blit(deathmessage_3,(0,0)) # if player has no lives left, game over
    pygame.display.update() # update display
    time.sleep(2) #freeze fror 2 seconds 
    if player.lives == 0:#if you have no lives left
        #player.lives = Penguin.lives # reset lives
        intro_screen() #return to intro screen

  

def unpause():# function to unpause the game
    global pause
    pygame.mixer.music.unpause() # resume music playback
    pause = False # set pause to False
 
def set_paused(): # function that calls paused after setting pause to True
    global pause
    pause = True 
    paused()

def paused(): # creates pause screen
    global pause
    pygame.mixer.music.pause() # stops music playback
     
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() # quit the game using specialised quit function 
        """
        Create a dedicated pause screen to blit:
        """
        
        gameDisplay.blit(pause_screen,(0,0)) # blit pause screen image to screen
        
        button("Continue",150,450,150,50,bright_orange,orange,unpause) # create button to unpause the game
        
        button("Quit",550,450,150,50,bright_orange,orange,quitgame) # create button to quit game
        
        pygame.display.update() # update the display
        clock.tick(15) # set FPS
        
def draw_to_screen():    # function to draw objects to the screen
    Background.Scroll(Background) # blit scrolling background and allow scrolling
    player.Life_Count() # display life count
    Rock.create_rock() # create rocks on keypress
    for projectile in Rock.projectiles:
        projectile.move_draw_check() # move_draw_check for each projectile in list
    player.display(player.x,player.y) # blit the player at x and y
    my_bird.update() # update bird flaps
    slow_bird.update()
    my_bird.move_draw_check() # move draw check for bird and seal
    my_seal.move_draw_check()
    if phase2 == True: # once phase 2 activated, draw extra bird+seal
        slow_bird.move_draw_check()
        slow_seal.move_draw_check()
    if BOSS == True: # once Boss activated, move_draw_check the boss and his barrels
        my_boss.move_draw_check()
        Barrel.createBarrel()
        for barrel in Barrel.barrels:
            barrel.move_draw_check()
 

def instruction_screen(): # create instruction screen
    instruction = True 
    instructionpic = pygame.image.load("Instructs fin.png") # load instruction png
    
    while instruction:# while instruction == true
        
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit() # if x in corner clicked, quit game
       
       gameDisplay.blit(instructionpic,(0,0)) # blit the picture at 0,0
    
       button("Back",50,510,150,50, bright_orange, orange, intro_screen) # create a back button
    
       pygame.display.update() # update pygame display
       clock.tick(15) # set FPS

def intro_screen():# function to create intro screen
    intro = True 
    pygame.mixer.music.stop() # stop music playback
    intropic = pygame.image.load("Intro Screen.png") # load the picture
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() # if red x clicked then quit game
        
        gameDisplay.blit(intropic, (0,0))# blit intropic to 0,0

        button("Play",150,450,150,50, bright_orange, orange,game_loop) # create play button that runs game_loop
        
        button("Quit",550,450,150,50, bright_orange, orange,quitgame) #create quit button that quits game
        
        button("Instructions",350, 520, 150, 50, bright_orange, orange, instruction_screen) # create instructions button that loads instructions page
        
        pygame.display.update() # update the display
        clock.tick(15) # set FPS


def epilogue_screen(): # Funciton for epilogue_screen
        pygame.mixer.music.stop() #stop the music
        gameDisplay.blit(epilogue_2,(0,0)) # blit each epilog picture, update display, and sleep for 2s
        pygame.display.update()
        time.sleep(2)
        gameDisplay.blit(epilogue_4,(0,0))
        pygame.display.update()
        time.sleep(2)
        gameDisplay.blit(epilogue_5,(0,0))
        pygame.display.update()
        time.sleep(2)
        intro_screen() # boot back to intro screen

def game_loop():
    global pause, phase2, my_seal, player, my_bird, my_boss, slow_seal, slow_bird, BOSS, phase2, already_run_message, epilogue, rock_count
    """
    Initialised variables and created objects - will reset each time game_loop() is run
    """
    
    BOSS = False
    exit = False
    phase2 = False # True when a certain number of enemies is killed to ramp up dificulty
    already_run_message = False
    epilogue = False
    my_seal = Seal(display_width,12) # Syntax - Class has capital, object is lowercase
    player = Penguin(Penguin.x,Penguin.y) 
    my_bird = Bird(display_width+ 300, 9)
    my_boss = Boss(display_width - 200, display_height - 400)

    slow_seal=Seal(display_width + 1000,10)
    slow_bird = Bird(display_width + 700, 7)
    pygame.mixer.music.play(-1) # loop music indefinitely 
    while exit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame() # if player clicks red x, quit game
        
        
        if my_seal.lives < 5 or my_bird.lives < 5: #condition for phase 2 activation
            phase2 = True 
        
        keys = pygame.key.get_pressed() # register key presses as "keys"
        
        if keys[pygame.K_p]: # if p is pressed, set pause to True and pause the game
            pause = True
            paused()
            
        if keys[pygame.K_LEFT]: # if left is pressed
            player.move("L") # run player.move with "l" params
        if keys[pygame.K_RIGHT]:
            player.move("R") # run player move method with "R" params
            
        if keys[pygame.K_SPACE]: # if spacebar is pressed
            jump.play() # play jump sound effect
            player.isJump = True # set isJump to true
        player.jump() # calls player.jump() - only does stuff if isJump == True 
        
        if epilogue == True: # if epilogue set to True
            epilogue_screen() # run epilogue screen

        rock_count +=1 # increase rock count each time game loop runs
        draw_to_screen() # draw to screen
        pygame.display.update() #update display
        clock.tick(30) # set fps
                
intro_screen() # run intro screen
pygame.quit() # quit pygame
os._exit(0) # quit for macs
quit # quit python