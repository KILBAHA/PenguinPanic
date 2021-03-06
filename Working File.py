"""
Initialisation:
"""
#Import modules:
import pygame
import time
import random
import math
#Initiate pygame:
pygame.init()
pygame.mixer.init()

#Set window
display_height=600
display_width=800
gameDisplay= pygame.display.set_mode((display_width, display_height)) # set display as gameDisplay
pygame.display.set_caption('Penguin Panic!')

#Set colours
black = (0,0,0) # takes RGB params
white = (255,255,255)
red = (200,0,0)
bright_red = (255,0,0)
green = (0,200,0)
bright_green = (0,255,0)
blue = (0,0,200)
bright_blue = (0,0,255)
orange = (242,176,21)
bright_orange = (247,210,64)

epilogue_0 = pygame.image.load("epilogue_0.png").convert()
epilogue_0 = pygame.transform.scale(epilogue_0, (display_width, display_height))
epilogue_1 = pygame.image.load("epilogue_1.png").convert()
epilogue_1 = pygame.transform.scale(epilogue_1, (display_width, display_height))
epilogue_2 = pygame.image.load("epilogue_2.png").convert()
epilogue_2 = pygame.transform.scale(epilogue_2, (display_width, display_height))
epilogue_3 = pygame.image.load("epilogue_3.png").convert()
epilogue_3 = pygame.transform.scale(epilogue_3, (display_width, display_height))
epilogue_4 = pygame.image.load("epilogue_4.png").convert()
epilogue_4 = pygame.transform.scale(epilogue_4, (display_width, display_height))
epilogue_5 = pygame.image.load("epilogue_5.png").convert()
epilogue_5 = pygame.transform.scale(epilogue_5, (display_width, display_height))


deathmessage_1 = pygame.image.load("Death Message 1.png")
deathmessage_1 = pygame.transform.scale(deathmessage_1,(display_width,display_height))
deathmessage_2 = pygame.image.load("Death Message 2.png")
deathmessage_2 = pygame.transform.scale(deathmessage_2,(display_width,display_height))
deathmessage_3 = pygame.image.load("Death message 3.png")
deathmessage_3 = pygame.transform.scale(deathmessage_3,(display_width,display_height))
pause_screen = pygame.image.load("Pause Screen.png")
pause_screen = pygame.transform.scale(pause_screen,(display_width,display_height))

#define clock
clock = pygame.time.Clock()

"""
Class Definitions
"""

class Background(): 
    
    bkgd = pygame.image.load("bg2.jpg").convert() 
    x = 0 # initial x
    
    def Scroll(self):
        rel_x = self.x % self.bkgd.get_rect().width 
        gameDisplay.blit(self.bkgd,(rel_x - self.bkgd.get_rect().width, 0)) #blit to rel_x minus width of background
        
        if rel_x <display_width:
            gameDisplay.blit(self.bkgd,(rel_x,0)) # gets rid of tear
        self.x -=1 # causes scrolling


class Penguin():
    
    penguinPic = pygame.image.load('Sliding Penguin.png') # variable for penguin sprite
    
    w = 130
    h = 80 # used for transformation, NOT ACTUAL WIDTH/HEIGHT!!!

    penguinPic = pygame.transform.scale(penguinPic,(w,h)) #transform penguin sprite
    
    width = penguinPic.get_rect().width
    height = penguinPic.get_rect().height

    isJump = False
    initial_jc = 16 # use to change size of jump
    JumpCount = initial_jc
    jump_lim = 0.2 # increase to increase jump height + jump acceleration/deceleration
    keys = pygame.key.get_pressed()
    lives = 5
    
    x = (display_width *0.0001) # initialise x and y (relative to display ) of penguin
    y = (display_height - (height-3))
    startx = x
    starty = y
    vx = 15
        
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def move(self,iput):
        if iput == "L":
            if self.x > self.vx:
                self.x -= self.vx
            else:
                pass
        if iput == "R":
            if self.x < display_width - self.width:
                self.x += self.vx
            else:
                pass


    
    def reset(self):
        self.isJump = False
        self.JumpCount = self.initial_jc
        self.x = self.startx
        self.y = self.starty
        
    def display(self,x,y):
        gameDisplay.blit(self.penguinPic,(x,y))
    
    def Life_Count(self):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Lives x{}".format(self.lives), True, black)
        gameDisplay.blit(text, (0,0))
        
    def jump(self):
        #jump.play()
        if self.isJump:
                if self.JumpCount >= -self.initial_jc:
                    neg = 1
                    if self.JumpCount < 0:
                        neg = -1
                    self.y -=(self.JumpCount**2)*self.jump_lim*neg
                    #jump.play()
                    self.JumpCount -= 1
                    
                    #jump.stop()
                else:
                    self.isJump = False
                    self.JumpCount = self.initial_jc

class Rock():
    
    rockPic = pygame.image.load("rock.png")
    w = 30
    h = 30
    rockPic = pygame.transform.scale(rockPic,(w,h))
    speed = 15
    projectiles = []
    
    def create_rock():
        keys = pygame.key.get_pressed()        
        
        if keys[pygame.K_UP]:
            if len(Rock.projectiles) < 100: #set this to 3
                Rock.projectiles.append(Rock(player.x +75, player.y +75, 100, 13))
             
    def resetrocks(self):
        for projectile in self.projectiles:
            self.projectiles.pop(self.projectiles.index(projectile))
            
    def __init__(self,x,y,itc,tc):
        self.x = x
        self.y = y
        self.itc = itc #initial throw count
        self.tc = tc # throw count
    
    def checkRock(self): # check off screen
        for projectile in self.projectiles:
            if projectile.x < display_width and projectile.y < display_height:
                pass
            else:
                self.projectiles.pop(self.projectiles.index(projectile))
    
    def move_draw_check(self):
        self.x += self.speed
        if self.tc >= -self.itc:
            neg = 1
            if self.tc < 0:
                neg = -1
            self.y -= (self.tc ** 2) * 0.4*neg
            self.tc -= 1
        gameDisplay.blit(self.rockPic,(self.x,self.y))
        self.checkRock()
       
       
class Enemy():
    lives = 10
    dodged = 0
    startx = display_width
    
    def reset_x(self):
        self.x = self.startx + random.randint(100, 300)
        
        
    def checkoffscreen(self):    
        if self.x <- self.width:
            Enemy.dodged+=1
            print ("dodged{}".format(Enemy.dodged))
            self.reset_x()
            
    def reset_all(self):
        my_bird.reset_x()
        my_seal.reset_x()
        slow_seal.reset_x()
        for barrel in Barrel.barrels:
            Barrel.barrels.pop(Barrel.barrels.index(barrel))

#can we bundle


    def checkrockcollision(self):
        global projectiles
        for projectile in Rock.projectiles:
#            if projectile.x > self.x and projectile.x + projectile.w > self.x:
#                print ("check 1")
#                if projectile.x < self.x + self.width and projectile.x + projectile.w < self.x + self.width:
#                    print ("check 2")
#                    if self.y > projectile.y and self.y < projectile.y + projectile.h or self.y + self.height > projectile.y and self.starty + self.height < projectile.y + projectile.h:
            if self.x < projectile.x and self.x + self.width > projectile.x + projectile.w:
                if projectile.y > self.y and self.y + self.width > projectile.y + projectile.h:
                    self.lives -=1   
                    Rock.resetrocks(Rock)
                    self.reset_x()    
                    rocksound.play()

    def checkcolision(self):
        if self.x < player.x + player.width and self.x > player.x or self.x + self.width < player.x + player.width and self.x + self.width > player.x:
            #if self.x + self.width < player.x + player.width and self.x + self.width > player.x:
            print ("x check")
            if self.y > player.y and self.y < player.y + player.height or self.y + self.height > player.y and self.y + self.height < player.y + player.height:
                player.lives -= 1
                livedown.play()
                self.reset_all()
                player.reset()
                Rock.resetrocks(Rock)
                Death()
                    
                    
    
    def move_draw_check(self):
        global BOSS
        if self.lives > 0:
            self.x -= self.speed
            self.y += self.vy
            if self.y <= 0:
                self.vy = -self.vy
            if self.y >= display_height - 300:
                self.vy = -self.vy
                
            #self.y -= self.vy
            #print (self.vy)
            self.draw()
            self.checkcolision()
            self.checkoffscreen()
            self.checkrockcollision()
        else:
            bossmessage()
            BOSS = True

class Barrel(Enemy):
    width = 68
    height = 68
    barrelPic = pygame.image.load("Oil Barrel.png")
    barrelPic = pygame.transform.scale(barrelPic,(width,height))
    vel = 15
    barrels = []
    
    def __init__(self, x, y): #tx and ty are target x and target y, to allow it to be thrown at the player
        self.x = x
        self.y = y
        self.tx = player.x
        self.ty = player.y
        self.startx = x
        self.starty = y
        self.x_diff = self.tx - self.startx
        self.y_diff = self.ty - self.starty
        self.angle = math.atan2(self.y_diff, self.x_diff)
        self.changex = math.cos(self.angle) * self.vel
        self.changey = math.sin(self.angle) * self.vel
    
    def draw(self):
        gameDisplay.blit(self.barrelPic,(self.x,self.y))
    
    def createBarrel():
        if len(Barrel.barrels) < 1:
            Barrel.barrels.append(Barrel(my_boss.x + 50, my_boss.y + 50))
            
    def check_offscreen(self):
        for barrel in self.barrels:
            if barrel.x < 0 - barrel.width or barrel.y > 600:
                self.barrels.pop(self.barrels.index(barrel))
                
            
    def move_draw_check(self):
        self.x += self.changex
        self.y += self.changey
        self.draw()
        self.checkcolision()
        self.check_offscreen()
        gameDisplay.blit(self.barrelPic,(self.x, self.y))

class Boss(Enemy):
    
    BossPic = pygame.image.load('bp_baloon.png') # variable for penguin sprite
    
    w = 145
    h = 285 # used for transformation, NOT ACTUAL WIDTH/HEIGHT!!!

    BossPic = pygame.transform.scale(BossPic,(w,h)) #transform penguin sprite
    
    lives = 3
    
    def __init__(self, x, y ):
        self.x = x
        self.y = y
        self.startx = x
        self.starty = y


    #finx = startx - 200
    width = 100
    height = 100
    vy = 3
    vx = -3

#    def checkrockcollision(self):
#        global projectiles
#        for projectile in Rock.projectiles:
##            if projectile.x > self.x and projectile.x + projectile.w > self.x:
##                print ("check 1")
##                if projectile.x < self.x + self.width and projectile.x + projectile.w < self.x + self.width:
##                    print ("check 2")
##                    if self.y > projectile.y and self.y < projectile.y + projectile.h or self.y + self.height > projectile.y and self.starty + self.height < projectile.y + projectile.h:
#            if self.x > projectile.x and self.x < projectile.x + projectile.w:
#                if projectile.y > self.starty or projectile.y > self.starty + self.height and projectile.y + projectile.h > self.starty or projectile.y + projectile.h > self.starty + self.height:
#                    self.lives -=1       
#                    rocksound.play()
 
    
    
    def draw(self):
        gameDisplay.blit(self.BossPic,(self.x,self.y))
    
    
    def reset_x(self):
        self.y = 1

    
    def move_draw_check(self):
        global epilogue
        
#        self.y += self.vy
#        self.x += self.vx
#        
#        if self.x >= self.startx and self.y <= display_height - 10:
#            self.vy = -3
#        if self.y <= display_height -10 and self.x >= self.startx - 200:
#            self.vy = 0
#            self.vx = -6
#        if self.x <= self.startx-200 
#            
                
        
        self.y += self.vy
        self.x += self.vx
        if self.y <= 0:
            self.vy = -self.vy
            #self.vx = +5
        if self.y >= display_height - (200+self.height):
            self.vy = -self.vy
            #self.vx = -5
        if self.x >= display_width + 100:
            self.vx = -self.vx
        if self.x <= display_width - 200:
            self.vx = -self.vx
        
        if self.lives > 0:
            self.draw()
            self.checkcolision()
            self.checkoffscreen()
            self.checkrockcollision()
        else:
            epilogue = True

class Bird(Enemy):
    
    
    birdPic1 = pygame.image.load('Bird1.png')
    birdPic2 = pygame.image.load('Bird2.png')
    
    w = 100
    h = 100 # used for transform - not actual width and height!
    
    birdPic1 = pygame.transform.scale(birdPic1, (w,h))
    birdPic2 = pygame.transform.scale(birdPic2,(w,h))
    
    width = birdPic1.get_rect().width
    height = birdPic1.get_rect().height
    
    starty = display_height - 400
    y = starty
    
    vy = 4
    
    def __init__(self,x,speed):
        self.x = x
        self.speed = speed
        
        self.images = []
        for i in range (3):
            self.images.append(self.birdPic1)
        for i in range(3):
            self.images.append(self.birdPic2)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(100, 100, 100, 100)
        
    def update(self):
        self.index += 1
        
        if self.index >= len(self.images):
            self.index = 0
            
        self.image = self.images[self.index]
        
    def draw(self):
        gameDisplay.blit(self.image,(self.x,self.y))


class Seal(Enemy):
    
   
    sealPic = pygame.image.load('Seal.png')
    
    w = 150
    h = 100 # used for transform - not actual width/height
    
    sealPic = pygame.transform.scale(sealPic,(w,h))
    
    width = sealPic.get_rect().width
    height = sealPic.get_rect().height
    
    starty = display_height - (height)
    vy = 0
    y = starty
    
    def __init__(self, x, speed ):
        self.x = x
        self.speed = speed
        
    def draw(self): 
        gameDisplay.blit(self.sealPic,(self.x,self.starty))
"""
class Text():
"""
"""
Create Objects from class:
"""



"""
Import Audio
"""

rocksound = pygame.mixer.Sound("rocksound.wav")
livedown = pygame.mixer.Sound("noot noot.wav")
jump = pygame.mixer.Sound("jump.wav")
pygame.mixer.music.load("dafeelin_loop.wav")

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

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    in_game_font = pygame.font.Font("freesansbold.ttf", 60)
    TextSurf, TextRect = text_objects(text, in_game_font)
    TextRect.center = ((display_width * 0.5), (display_height * 0.5))
    gameDisplay.blit(TextSurf, TextRect)
    
def bossmessage():
    global already_run_message
    
    if already_run_message == True:
        pass
    else:
        message_display("Warning! Boss Incoming!")
        pygame.display.update()
        time.sleep(2)
        already_run_message = True

def Death():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

    if player.lives >=2:
        gameDisplay.blit(deathmessage_1,(0,0))
    elif player.lives == 1:
        gameDisplay.blit(deathmessage_2,(0,0))
    else:
        gameDisplay.blit(deathmessage_3,(0,0))
    pygame.display.update()
    time.sleep(2)
    if player.lives == 0:
        #livedown.play()
        player.lives = Penguin.lives
        intro_screen()

  

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False
 
def set_paused():
    global pause
    pause = True
    paused()

def paused():
    global pause
    pygame.mixer.music.pause()
     
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        """
        Create a dedicated pause screen to blit:
        """
        
        gameDisplay.blit(pause_screen,(0,0))
        
        button("Continue",150,450,150,50,bright_orange,orange,unpause) # x,y,w,h,ac,ic,fn
        
        button("Quit",550,450,150,50,bright_orange,orange,quitgame)
        
        pygame.display.update()
        clock.tick(15)
        
def draw_to_screen():    
    Background.Scroll(Background)
    player.Life_Count()
    Rock.create_rock()
    for projectile in Rock.projectiles:
        projectile.move_draw_check()
    #button("Pause",400,450,150,50,green,bright_green,set_paused)
    player.display(player.x,player.y)
    my_bird.update()
    slow_bird.update()
    my_bird.move_draw_check()
    my_seal.move_draw_check()
    if phase2 == True:
        slow_bird.move_draw_check()
        slow_seal.move_draw_check()
    if BOSS == True:
        my_boss.move_draw_check()
        Barrel.createBarrel()
        for barrel in Barrel.barrels:
            barrel.move_draw_check()
    
#def checkrockcollision():
#    global projectiles
#    for projectile in projectiles:
#        if my_bird.x < projectile.x + projectile.w and my_bird.x > projectile.x:
#                        if my_bird.x + my_bird.w < projectile.x + projectile.w and my_bird.x + my_bird.w > projectile.x:
#                            if my_bird.starty > projectile.y and my_bird.starty < projectile.y + projectile.h or my_bird.starty + my_bird.height > projectile.y and my_bird.starty + my_bird.height < projectile.y + projectile.h:
#                                my_bird.reset_x()
#                                print("Hit")
 

def instruction_screen():
    instruction = True
    instructionpic = pygame.image.load("Instructs fin.png")
    
    while instruction:
        
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()
       
       gameDisplay.blit(instructionpic,(0,0))
    
       button("Back",50,510,150,50, bright_orange, orange, intro_screen)
    
       pygame.display.update()
       clock.tick(15)

def intro_screen():
    intro = True
    pygame.mixer.music.stop()
    intropic = pygame.image.load("Intro Screen.png")
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.blit(intropic, (0,0))
        """largeText = pygame.font.Font ('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects("Penguin Panic!", largeText)
        TextRect.center = ((display_width * 0.5),(display_height * 0.5))
        gameDisplay.blit(TextSurf, TextRect)"""
        
        button("Play",150,450,150,50, bright_orange, orange,game_loop) # x,y,w,h,ac,ic,fn
        
        button("Quit",550,450,150,50, bright_orange, orange,quitgame)
        
        button("Instructions",350, 520, 150, 50, bright_orange, orange, instruction_screen)
        
        pygame.display.update()
        clock.tick(15)


def epilogue_screen():
        global epilogue_0, epilogue_1, epilogue_2, epilogue_3, epilogue_4, epilogue_5  
        pygame.mixer.music.stop()
        gameDisplay.blit(epilogue_1,(0,0))
        pygame.display.update()
        time.sleep(2)
        gameDisplay.blit(epilogue_2,(0,0))
        pygame.display.update()
        time.sleep(2)
        gameDisplay.blit(epilogue_4,(0,0))
        pygame.display.update()
        time.sleep(2)
        gameDisplay.blit(epilogue_5,(0,0))
        pygame.display.update()
        time.sleep(2)
        intro_screen()



"""
Create the gameloop:
"""

def game_loop():
    global pause, phase2, my_seal, player, my_bird, my_boss, slow_seal, slow_bird, BOSS, phase2, already_run_message, epilogue
    BOSS = False
    exit = False
    phase2 = False
    already_run_message = False
    epilogue = False
    my_seal = Seal(display_width,12) # Syntax - Class has capital, object is lowercase
    player = Penguin(Penguin.x,Penguin.y) 
    my_bird = Bird(display_width+ 300, 9)
    my_boss = Boss(display_width - 200, display_height - 400)

    slow_seal=Seal(display_width + 1000,10)
    slow_bird = Bird(display_width + 700, 7)
    #soundtrack.play()
    pygame.mixer.music.play(-1)
    while exit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True  
        
        
        if my_seal.lives < 5 or my_bird.lives < 5:
            phase2 = True
        
        keys = pygame.key.get_pressed()        
        
        if keys[pygame.K_p]:
            pause = True
            paused()
            
        if keys[pygame.K_LEFT]:
            player.move("L")
        if keys[pygame.K_RIGHT]:
            player.move("R")
            
        if keys[pygame.K_SPACE]:
            jump.play()
            player.isJump = True
        player.jump()
        
        if epilogue == True:
            epilogue_screen()

        draw_to_screen()
        pygame.display.update()
        clock.tick(30)
                
intro_screen()
pygame.quit()
quit