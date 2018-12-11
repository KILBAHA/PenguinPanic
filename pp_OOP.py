import pygame
import time
import random
import math

pygame.init()
pygame.mixer.init()


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