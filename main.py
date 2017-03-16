import pygame

#----------------------------------Functions that need to iniatize to run games. -------------#
pygame.init()

#RGB colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

# The functions parameter must be a tuple, which means that you need do within semicolons ()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')


# pygame.display.flip() is working like update,but flip is going to update the whole surface.
pygame.display.update()

#---------------------------------------------------------------------------------------------#

#----------------------------------Functions to run the game.------------------- -------------#
gameExit = False

#The leader of group of the blocks that is the snake. Head of the snake.
lead_x = 300
lead_y = 300

# Variable to success when you press down a key it continue.
lead_x_change = 0

# Variable to decide frame/sec
clock = pygame.time.Clock()


while not gameExit:
    for event in pygame.event.get():
        #So we can exit the game through the X button in the game window.
        if event.type == pygame.QUIT:
            gameExit = True
        #print(event)

        #The logic for the movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                #lead_x -= 10
                lead_x_change = -10
            if event.key == pygame.K_RIGHT:
                #lead_x += 10
                lead_x_change = 10

    # This logic is used if you want the movement stops if you drop the key.
    #if event.type == pygame.KEYUP:
    #   if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
    #       lead_x_change = 0

    lead_x += lead_x_change

    gameDisplay.fill(white)
    # Parameters are, where to draw it, which color, size
    pygame.draw.rect(gameDisplay, black, [lead_x,lead_y, 10,10])
    pygame.display.update()

    #Parameter is the frame/sec, 30 is standard. 15 for Snake game is okey.
    clock.tick(15)

# ---------------------------------------------------------------------------------------------#

#----------------------------------Functions that need to quit the game. ---------------------#
pygame.quit()
quit()
#---------------------------------------------------------------------------------------------#