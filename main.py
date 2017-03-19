import pygame
import time
import random


#----------------------------------Functions that need to iniatize to run games. -------------#
pygame.init()

#RGB colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

#The variables for the gameDisplay size.
display_width = 800
display_height = 600

# Variable for the FramePerSecond that uses for the speed in the game.
FramePerSecond = 15

# The functions parameter must be a tuple, which means that you need do within semicolons ()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')


# pygame.display.flip() is working like update,but flip is going to update the whole surface.
pygame.display.update()

#---------------------------------------------------------------------------------------------#

#----------------------------------Functions to run the game.------------------- -------------#

# Variable to decide frame/sec
clock = pygame.time.Clock()

#Variable for the block size for the snake.
block_size = 20

# Create a font object
font = pygame.font.SysFont(None, 25)

#Function to create the snake.
def snake(block_size, snakeList):
    for XandY in snakeList:
        # Parameters are, where to draw it, which color, size
        pygame.draw.rect(gameDisplay, green, [XandY[0], XandY[1], block_size, block_size])


# Function to write out message to the user
def message_to_screen(message, color):
    screen_text = font.render(message, True, color)

    # the blit function takes the parameters and add them to the screen.
    gameDisplay.blit(screen_text, [display_width/2,display_height/2])



#------------------------ gameLoop Function -----------------------------#
def gameLoop():
    gameExit = False
    gameOver = False

    # The leader of group of the blocks that is the snake. Head of the snake.
    lead_x = display_width / 2
    lead_y = display_height / 2

    # Variable to success when you press down a key it continue.
    lead_x_change = 0
    lead_y_change = 0

    #The array that is going to be the snake body.
    snakeList = []
    snakeLength = 1

    #Variables for the apple. Need to be -block_size so the apple does not appear outside the display.
    #We use round to get the apple perfect align to compare to the snake.

    randAppleX = round(random.randrange(0,display_width-block_size)) #/10.0)* 10.0
    randAppleY = round(random.randrange(0,display_height-block_size))#/10.0)*10.0

    while not gameExit:

        while gameOver == True:

            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False

                    elif event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            #So we can exit the game through the X button in the game window.
            if event.type == pygame.QUIT:
                gameOver = True
            #print(event)

        # ----------------------Logic for the movement---------------------------------------------------#
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #lead_x -= 10
                    lead_x_change = -block_size
                    #We need to change y also so we dont get the snake to run diagonal.
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    #lead_x += 10
                    lead_x_change = block_size
                    lead_y_change = 0

                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    # We need to change x also so we dont get the snake to run diagonal.
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        # ----------------------------------------------------------------------------------------------------#

        # -------------------------The boundaries logic-------------------------------------------------------#
            # Checking if snake is over the gameDisplay limits.
        if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
            gameOver = True


        # This logic is used if you want the movement stops if you drop the key.
        #if event.type == pygame.KEYUP:
        #   if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #       lead_x_change = 0

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)

        applethickness = 30
        #The order by draw items is important, you want the item that is most important draw last, in our case the snake.
        pygame.draw.rect(gameDisplay, red, [randAppleX,randAppleY, applethickness,applethickness])

        #The array that is going to extend the snake.
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        #Need this condition to so the snake does not getting constant bigger.
        if len(snakeList) > snakeLength:
            del snakeList[0]

        #Loop to check if we get a overleap in our snake, the loope goes throw all the list except
        #the head of the snake (:-1).  Doing so to prevent so user can't change directions and run over the snake.
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)

        pygame.display.update()
        # -----------------------------------------------------------------------------------------------#


        # -------------------------The apple logic-------------------------------------------------------#
        # When the snake eats the apple.

        '''
        if lead_x >= randAppleX and lead_x <= randAppleX + applethickness:
            if lead_y >= randAppleY and lead_y <= randAppleY + applethickness:
                randAppleX = round(random.randrange(0, display_width - block_size))# / 10.0) * 10.0
                randAppleY = round(random.randrange(0, display_height - block_size))# / 10.0) * 10.0
                snakeLength += 1
        # ---------------------------------------------------------------------------------------------#
        '''
        if lead_x > randAppleX and lead_x < randAppleX + applethickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + applethickness:
            #print "x crossover"
            if lead_y > randAppleY and lead_y < randAppleY + applethickness:
                randAppleX = round(random.randrange(0, display_width - block_size))  # / 10.0) * 10.0
                randAppleY = round(random.randrange(0, display_height - block_size))  # / 10.0) * 10.0
                snakeLength += 1

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + applethickness:
                randAppleX = round(random.randrange(0, display_width - block_size))# / 10.0) * 10.0
                randAppleY = round(random.randrange(0, display_height - block_size))# / 10.0) * 10.0
                snakeLength += 1
                
        # Parameter is the frame/sec, 30 is standard. 15 for Snake game is okey.
        clock.tick(FramePerSecond)

    # ---------------------------------------------------------------------------------------------#

    #----------------------------------Functions that needs to quit the game. ---------------------#
    pygame.quit()
    quit()
    # ---------------------------------------------------------------------------------------------#


#---------------------------------gameLoop function ends---------------------------------------------#

gameLoop()