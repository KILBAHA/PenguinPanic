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

rock_count = 0


#define clock
clock = pygame.time.Clock()

rocksound = pygame.mixer.Sound("rocksound.wav")
livedown = pygame.mixer.Sound("noot noot.wav")
jump = pygame.mixer.Sound("jump.wav")
pygame.mixer.music.load("dafeelin_loop.wav")