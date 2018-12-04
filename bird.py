import pygame

Size = width, height = 600, 800 #the width and height of our screen
background = pygame.Color('white') #The background colod of our window
FPS = 30 #Frames per second

display_height = 600
display_width = 800
gameDisplay= pygame.display.set_mode((display_width, display_height))

class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super(Sprite, self).__init__()
        #adding all the images to sprite array
        self.images = []
        self.images.append(pygame.image.load('ShitBird1.png'))
        self.images.append(pygame.image.load('ShitBird2 (2).png'))
        
        #index value to get the image from the array
        #initially it is 0 
        self.index = 0
        #now the image that we will display will be the index from the image array 
        self.image = self.images[self.index]
        #creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite 
        self.rect = pygame.Rect(100, 100, 100, 100)
    def update(self):
        #when the update method is called, we will increment the index
        self.index += 1
 
        #if the index is larger than the total images
        if self.index >= len(self.images):
            #we will make the index to 0 again
            self.index = 0
        
        #finally we will update the image that will be displayed
        self.image = self.images[self.index]
    def draw(self):
        gameDisplay.blit(self.image,(0,0))
        

def main():
    pygame.init()
    #screen = pygame.display.set_mode(Size)
    #creating our sprite object
    my_sprite = Sprite()
    #my_group = pygame.sprite.Group(my_sprite)#creating a group with our sprite
    clock = pygame.time.Clock()
 
    while True:
        #getting the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
        my_sprite.update()
        gameDisplay.fill(background)
        my_sprite.draw()
        pygame.display.update()
        clock.tick(10)
main()