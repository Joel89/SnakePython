import pygame

#----------------------------------Functions that need to iniatize to run games. -------------#
pygame.init()

# The functions parameter must be a tuple, which means that you need do within semicolons ()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')

# pygame.display.flip() is working like update,but flip is going to update the whole surface.
pygame.display.update()

#---------------------------------------------------------------------------------------------#

#----------------------------------Functions to run the game.------------------- -------------#
gameExit = False

while not gameExit:
    for event in pygame.event.get():
        #So we can exit the game through the X button in the game window.
        if event.type == pygame.QUIT:
            gameExit = True
        #print(event)



# ---------------------------------------------------------------------------------------------#

#----------------------------------Functions that need to quit the game. ---------------------#
pygame.quit()
quit()
#---------------------------------------------------------------------------------------------#