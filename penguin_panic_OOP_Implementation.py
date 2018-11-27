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

pause = False

#define clock
clock = pygame.time.Clock()

class Background():
    bkgd = pygame.image.load("bg2.jpg").convert()
    bgx = 0
    
    def Scroll(self):
        gameDisplay.blit(self.bkgd, (self.bgx, 0))
        self.bgx -=1

class Penguin():
    
    penguinPic = pygame.image.load('Resized Penguin.png')
    
    w = 150
    h = 150
    
    penguinPic = pygame.transform.scale(penguinPic,(w,h))
    
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
    
    def createEnemy():
        pass

class Seal(Enemy):
    
    startx = display_width
    x = startx
    starty = display_height - 110
    speed = 12
    width = 100
    height = 100
    
    def createSeal(self):
        pygame.draw.rect(gameDisplay, blue, [self.x, self.starty, self.width, self.height])
        
    def reset_sealx():
        Seal.x = Seal.startx
"""
class Text():
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
            
    Seal.reset_sealx()

    if Penguin.lives >=2:
        message_display("You died, {} lives remaining".format(Penguin.lives))
    elif Penguin.lives == 1:
        message_display("You died, 1 life remaining")
    else:
        message_display("Game Over")
    pygame.display.update()
    time.sleep(2)
    if Penguin.lives == 0:
        intro_screen()

  
def checkoffscreen():
    if Seal.x <-Seal.width:
        Enemy.dodged+=1
        print ("dodged{}".format(Seal.dodged))
        Seal.reset_sealx()
      
def checkcolision():
    if Seal.x > Penguin.x and Seal.x < Penguin.x + Penguin.w:
        #print("xcheck")
        if Penguin.y > Seal.starty or Penguin.y > Seal.starty + Seal.height and Penguin.y + Penguin.h > Seal.starty or Penguin.y + Penguin.h > Seal.starty + Seal.height:
            Penguin.lives -= 1
            Death()

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
    Background.Scroll(Background)
    #button("Pause",400,450,150,50,green,bright_green,paused)
    Seal.createSeal(Seal)
    Seal.x -= Seal.speed
    Penguin.display(Penguin,Penguin.x,Penguin.y)
    checkcolision()
    checkoffscreen()

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
    global pause
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
                Penguin.y-= (JumpCount **2)*0.25 * neg
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
    
    