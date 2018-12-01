import pygame

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type ==pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            
"""            
define display surface:			
"""
W, H = 800, 600
"""
initialise display
"""
pygame.init()
gameDisplay = pygame.display.set_mode((W, H))


bkgd = pygame.image.load("bg2.jpg")
x = 0
#rel_x = x % bkgd.get_rect().width

clock = pygame.time.Clock()  
 
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type ==pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
    
    rel_x = x % bkgd.get_rect().width
    gameDisplay.blit(bkgd,(rel_x - bkgd.get_rect().width, 0))
    
    if rel_x < W:
        gameDisplay.blit(bkgd,(rel_x, 0))
    
    clock.tick(300)
    pygame.display.update()    
    
    x -=1    
pygame.quit()
quit
    
    