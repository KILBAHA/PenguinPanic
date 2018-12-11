import pygame
import time
import random
import math

pygame.init()
pygame.mixer.init()


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