"""
Initialisation:
"""
#Import modules:
import pygame
import time

#Initiate pygame:
pygame.init()

#Set window
display_height=600
display_width=800
gameDisplay= pygame.display.set_mode((display_width, display_height))
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

#pause = False

#define clock
clock = pygame.time.Clock()

"""
Class Definitions
"""

class Background(): 
    
    bkgd = pygame.image.load("bg2.jpg").convert()
    bgx = 0
    
    def Scroll(self):
        gameDisplay.blit(self.bkgd, (self.bgx, 0)) #        gameDisplay.fill(bkgd)
        self.bgx -=1

class Penguin():
    
    penguinPic = pygame.image.load('Resized Penguin.png') # variable for penguin sprite
    
    w = 150
    h = 150
    
    penguinPic = pygame.transform.scale(penguinPic,(w,h)) #transform penguin sprite
    
    lives = 3
    
    x = (display_width *0.0001) # initialise x and y (relative to display ) of penguin
    y = (display_height * 0.75)
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def display(self,x,y):
        gameDisplay.blit(self.penguinPic,(x,y))
    
    def Life_Count(self):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Lives x{}".format(self.lives), True, black)
        gameDisplay.blit(text, (0,0))
        
class Enemy():
    
    dodged = 0

class Seal(Enemy):
    
    startx = display_width
    starty = display_height - 110
    width = 100
    height = 100
    
    def __init__(self, x, speed ):
        self.x = x
        self.speed = speed
        
    def drawseal(self):
        pygame.draw.rect(gameDisplay, blue, [self.x, self.starty, self.width, self.height])
        
    def reset_sealx(self):
        self.x = self.startx
        
    def checkoffscreen(self):
    #global my_seal
    
        if self.x <- self.width:
            Enemy.dodged+=1
            print ("dodged{}".format(Enemy.dodged))
            self.reset_sealx()
      
    def checkcolision(self):
    #global my_seal
    
        if self.x > player.x and self.x < player.x + player.w:
            #print("xcheck")
            if player.y > self.starty or player.y > self.starty + self.height and player.y + player.h > self.starty or player.y + player.h > self.starty + self.height:
                player.lives -= 1
                self.reset_sealx()
                Death()
<<<<<<< HEAD
    
    def move_draw_check(self):
        self.x -= self.speed
        self.draw()
        self.checkcolision()
        self.checkoffscreen()
    
class Bird(Enemy):
    
    birdPic1 = pygame.image.load('ShitBird1.png')
    birdPic2 = pygame.image.load('ShitBird2 (2).png')
    w = 100
    h = 100
    
    birdPic1 = pygame.transform.scale(birdPic1, (w,h))
    birdPic2 = pygame.transform.scale(birdPic2,(w,h))
    
    starty = display_height - 400
    
    width = 100
    height = 100
    
    
    def __init__(self,x,speed):
        super(Bird, self).__init__()
        self.x = x
        self.speed = speed
        #super(Bird, self).__init__()
        self.images = []
        self.images.append(self.birdPic1)
        self.images.append(self.birdPic2)       
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(self.x, self.starty, 100, 100)
        
    def update(self):
        self.index += 1
 
        #if the index is larger than the total images
        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]
        
    def draw(self):
        gameDisplay.blit(self.birdPic,(self.x,self.starty))
        
#class Bird(Enemy):
#    def __init__(self):
#        super(Bird, self).__init__()
#        self.images = []
#        self.images.append(pygame.image.load('ShitBird1.png'))
#        self.images.append(pygame.image.load('ShitBird2 (2).png'))       
#        self.index = 0
#        self.image = self.images[self.index]
#        self.rect = pygame.Rect(100, 100, 100, 100)
#        
#    def update(self):
#        self.index += 1
# 
#        #if the index is larger than the total images
#        if self.index >= len(self.images):
#            self.index = 0
#        
#        self.image = self.images[self.index]


class Seal(Enemy):
    
    width = 100
    height = 100
    
    starty = display_height - 100
    
    sealPic = pygame.image.load('Seal.png')
    
    w = 100
    h = 100
    
    sealPic = pygame.transform.scale(sealPic,(w,h))
    
    def __init__(self, x, speed ):
        self.x = x
        self.speed = speed
        
    def draw(self): 
        gameDisplay.blit(self.sealPic,(self.x,self.starty))
=======
>>>>>>> parent of 9d33823... Factored out and added sprites
"""
class Text():
"""

"""
Create Objects from class:
"""
my_seal = Seal(display_width,12) # Syntax - Class has capital, object is lowercase
slow_seal=Seal(display_width,5)
player = Penguin(Penguin.x,Penguin.y) 
<<<<<<< HEAD
my_bird = Bird(display_width+ 300, 12)
my_group = pygame.sprite.Group(my_bird)
=======
>>>>>>> parent of 9d33823... Factored out and added sprites

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
            
    #my_seal.reset_sealx()

    if player.lives >=2:
        message_display("You died, {} lives remaining".format(player.lives))
    elif player.lives == 1:
        message_display("You died, 1 life remaining")
    else:
        message_display("Game Over")
    pygame.display.update()
    time.sleep(2)
    if player.lives == 0:
        intro_screen()

  
#def checkoffscreen():
#    global my_seal
#    
#    if my_seal.x <- my_seal.width:
#        Enemy.dodged+=1
#        print ("dodged{}".format(Enemy.dodged))
#        my_seal.reset_sealx()
#      
#def checkcolision():
#    global my_seal
#    
#    if my_seal.x > player.x and my_seal.x < player.x + player.w:
#        #print("xcheck")
#        if player.y > my_seal.starty or player.y > my_seal.starty + my_seal.height and player.y + player.h > my_seal.starty or player.y + player.h > my_seal.starty + my_seal.height:
#            player.lives -= 1
#            Death()

# =============================================================================
# def unpause():
#     global pause
#     pause = False
# 
#   
# def paused():
# 
#     
#     while pause:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#         
#         gameDisplay.fill(white)
#         
#         largeText = pygame.font.Font ('freesansbold.ttf', 100)
#         TextSurf, TextRect = text_objects("Paused", largeText)
#         TextRect.center = ((display_width * 0.5),(display_height * 0.5))
#         gameDisplay.blit(TextSurf, TextRect)
#         
#         button("Continue",150,450,150,50,green,bright_green,unpause) # x,y,w,h,ac,ic,fn
#         
#         button("Quit",550,450,150,50,red,bright_red,quitgame)
#         
#         pygame.display.update()
#         clock.tick(15)
# =============================================================================

def draw_to_screen():
    
    global my_seal
    
    Background.Scroll(Background)
    #button("Pause",400,450,150,50,green,bright_green,paused)
    my_seal.x -= my_seal.speed
    slow_seal.x -= slow_seal.speed
    my_seal.drawseal()
    slow_seal.drawseal()
    player.display(player.x,player.y)
<<<<<<< HEAD
    #my_group = pygame.sprite.Group(my_bird)
    screen = pygame.display.set_mode()
    my_bird.move_draw_check()
    my_seal.move_draw_check()
    slow_seal.move_draw_check()
    my_group.update()
    gameDisplay.fill(Background.bkgd)
    pygame.display.update()        
    my_group.draw(screen)
    

=======
    my_seal.checkcolision()
    slow_seal.checkcolision()
    my_seal.checkoffscreen()
    slow_seal.checkoffscreen()
>>>>>>> parent of 9d33823... Factored out and added sprites

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
    #global pause
    exit = False
    
    isJump = False
    initial_jc = 13
    JumpCount = initial_jc

    
    while exit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
                
        keys = pygame.key.get_pressed()        
        
        if not (isJump):
            if keys[pygame.K_SPACE]:
                isJump = True
                
        else:
            if JumpCount >= -initial_jc:
                neg = 1
                if JumpCount < 0:
                    neg =-1
                player.y-= (JumpCount **2)*0.25 * neg
                JumpCount -=1
            else:
                isJump=False
                JumpCount = initial_jc

        draw_to_screen()
        pygame.display.update()
        clock.tick(30)
                

intro_screen()
pygame.quit()
quit
    
    