import pygame
import time

#----------------------------------Functions that need to iniatize to run games. -------------#
pygame.init()

#RGB colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

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
block_size = 10

# Create a font object
font = pygame.font.SysFont(None, 25)

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

    while not gameExit:

        while gameOver == True:

            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
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

            #The logic for the movement
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

        #The boundaries logic
            # Checking if snake is over the gameDisplay limits.
        if lead_x_change >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
            gameOver = True


        # This logic is used if you want the movement stops if you drop the key.
        #if event.type == pygame.KEYUP:
        #   if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #       lead_x_change = 0

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)
        # Parameters are, where to draw it, which color, size
        pygame.draw.rect(gameDisplay, black, [lead_x,lead_y, block_size,block_size])
        pygame.display.update()

        #Parameter is the frame/sec, 30 is standard. 15 for Snake game is okey.
        clock.tick(FramePerSecond)

    # ---------------------------------------------------------------------------------------------#

    #----------------------------------Functions that need to quit the game. ---------------------#
    pygame.quit()
    quit()
#---------------------------------gameLoop function ends---------------------------------------------#

gameLoop()