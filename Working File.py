"""
Initialisation:
"""
#Import modules:
import pygame
import time
import random
#Initiate pygame:
pygame.init()

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
pause = False  # required for pause function

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
    
    w = 185
    h = 100 # used for transformation, NOT ACTUAL WIDTH/HEIGHT!!!

    penguinPic = pygame.transform.scale(penguinPic,(w,h)) #transform penguin sprite
    
    width = penguinPic.get_rect().width
    height = penguinPic.get_rect().height

    isJump = False
    initial_jc = 13 # use to change size of jump
    JumpCount = initial_jc
    jump_lim = 0.3 # increase to increase jump height + jump acceleration/deceleration
    keys = pygame.key.get_pressed()
    lives = 3
    
    """
    sort this shit out!:
    """
    
    x = (display_width *0.0001) # initialise x and y (relative to display ) of penguin
    y = (display_height * 0.75)
    startx = x
    starty = y
        
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
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
        if self.isJump:
                if self.JumpCount >= -self.initial_jc:
                    neg = 1
                    if self.JumpCount < 0:
                        neg = -1
                    self.y -=(self.JumpCount**2)*self.jump_lim*neg
                    self.JumpCount -= 1
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
         if len(Rock.projectiles) < 100:
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

#can we bundle


    def checkrockcollision(self):
        global projectiles
        for projectile in Rock.projectiles:
            if self.x > projectile.x and self.x < projectile.x + projectile.w:
                if projectile.y > self.starty or projectile.y > self.starty + self.height and projectile.y + projectile.h > self.starty or projectile.y + projectile.h > self.starty + self.height:
                    self.reset_x()        

    def checkcolision(self):
        if self.x < player.x + player.width and self.x > player.x:
            if self.x + self.width < player.x + player.width and self.x + self.width > player.x:
                if self.starty > player.y and self.starty < player.y + player.height or self.starty + self.height > player.y and self.starty + self.height < player.y + player.height:
                    player.lives -= 1
                    self.reset_all()
                    player.reset()
                    Death()
                    
    
    def move_draw_check(self):
        self.x -= self.speed
        self.y += self.vy
        if self.y <= 0:
            self.vy = -self.vy
        if self.y >= display_height - 300:
            self.vy = -self.vy
            
        #self.y -= self.vy
        print (self.vy)
        self.draw()
        self.checkcolision()
        self.checkoffscreen()
        self.checkrockcollision()
    
class Bird(Enemy):
    
    birdPic1 = pygame.image.load('Shitbird1.png')
    birdPic2 = pygame.image.load('ShitBird2 (2).png')
    
    w = 100
    h = 100 # used for transform - not actual width and height!
    
    birdPic1 = pygame.transform.scale(birdPic1, (w,h))
    birdPic2 = pygame.transform.scale(birdPic2,(w,h))
    
    width = birdPic1.get_rect().width
    height = birdPic1.get_rect().height
    
    starty = display_height - 400
    y = starty
    
    vy = 6
    
    def __init__(self,x,speed):
        self.x = x
        self.speed = speed
        
        self.images = []
        self.images.append(self.birdPic1)
        self.images.append(self.birdPic1)
        self.images.append(self.birdPic1)
        self.images.append(self.birdPic2)
        self.images.append(self.birdPic2)
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
    
    width = 100
    height = 100
    
    starty = display_height - 100
    vy = 0
    y = starty
    
    sealPic = pygame.image.load('Seal.png')
    
    w = 100
    h = 100 # used for transform - not actual width/height
    
    sealPic = pygame.transform.scale(sealPic,(w,h))
    
    width = sealPic.get_rect().width
    height = sealPic.get_rect().height
    
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
my_seal = Seal(display_width,12) # Syntax - Class has capital, object is lowercase
slow_seal=Seal(display_width + 500,12)
player = Penguin(Penguin.x,Penguin.y) 
my_bird = Bird(display_width+ 300, 12)


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

def Death():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

    if player.lives >=2:
        message_display("You died, {} lives remaining".format(player.lives))
    elif player.lives == 1:
        message_display("You died, 1 life remaining")
    else:
        message_display("Game Over")
    pygame.display.update()
    time.sleep(2)
    if player.lives == 0:
        player.lives = Penguin.lives
        intro_screen()

  

def unpause():
    global pause
    pause = False
 
def set_paused():
    global pause
    pause = True
    paused()

def paused():
    global pause
     
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
         
        gameDisplay.fill(white)
        
        largeText = pygame.font.Font ('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width * 0.5),(display_height * 0.5))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("Continue",150,450,150,50,green,bright_green,unpause) # x,y,w,h,ac,ic,fn
        
        button("Quit",550,450,150,50,red,bright_red,quitgame)
        
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
    my_bird.move_draw_check()
    my_seal.move_draw_check()
    slow_seal.move_draw_check()
    
#def checkrockcollision():
#    global projectiles
#    for projectile in projectiles:
#        if my_bird.x < projectile.x + projectile.w and my_bird.x > projectile.x:
#                        if my_bird.x + my_bird.w < projectile.x + projectile.w and my_bird.x + my_bird.w > projectile.x:
#                            if my_bird.starty > projectile.y and my_bird.starty < projectile.y + projectile.h or my_bird.starty + my_bird.height > projectile.y and my_bird.starty + my_bird.height < projectile.y + projectile.h:
#                                my_bird.reset_x()
#                                print("Hit")
        

def intro_screen():
    intro = True
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
        
        button("Instructions",350, 520, 150, 50, bright_orange, orange)
        
        pygame.display.update()
        clock.tick(15)







"""
Create the gameloop:
"""

def game_loop():
    global pause
    exit = False
    
    
    while exit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
                
        keys = pygame.key.get_pressed()        
        
        if keys[pygame.K_p]:
            pause = True
            paused()
            
        
        if keys[pygame.K_SPACE]:
            player.isJump = True
        player.jump()

        
        
        draw_to_screen()
        pygame.display.update()
        clock.tick(30)
                

intro_screen()
pygame.quit()
quit