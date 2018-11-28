import pygame

# exit the program
def events():
    pass
            
# define display surface			
W, H = 800, 600
#HW, HH = W / 2, H / 2
#AREA = W * H

# initialise display
pygame.init()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Scrolling Background with Player")

bkgd = pygame.image.load("bg2.jpg").convert()
x = 0
rel_x = x % bkgd.get_rect().width 
 #    gameDisplay.fill(white)  set the background to white   
 
while True:
    events()
    DS.blit(bkgd, (rel_x - bkgd.get_rect().width, 0))	
    if rel_x < W:
        DS.blit(bkgd, (rel_x, 0))  
    x -=1
    pygame.display.update()
    
pygame.quit()
quit
    
    