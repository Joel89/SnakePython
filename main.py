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

# Loading up the snakehead image and apple image that is in the same folder as the main python file.
img = pygame.image.load('snakehead.png')
appleimg = pygame.image.load('apple.png')

# different alternative to the snake to eat.
frogimg = pygame.image.load('frog.png')
pacmanimg = pygame.image.load('pacman.png')

#Variable that is used to rotate the snakehead image. Namned it Right because it is the direction it begins with.
direction = "right"

# pygame.display.flip() is working like update,but flip is going to update the whole surface.
pygame.display.update()

#---------------------------------------------------------------------------------------------#

#----------------------------------Functions to run the game.------------------- -------------#

# Variable to decide frame/sec
clock = pygame.time.Clock()

#Variable for the block size for the snake.
block_size = 20

# Creates different font objects so we can use different font size and styles.
# smallfont = pygame.font.Font(None, 25) is used to when you want a font from ex Google.
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

#Function for the start menu.
def game_intro():
    intro = True

    while intro:

        # Response to the user input.
        for event in pygame.event.get():
            #So the user can quit by clicking the X window button.
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #If the user click on the keyboard.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)

        # y_displace and size are parameter default, does not need to write out but get better overview to display the
        # variable names.
        message_to_screen("Welcome to Slither",
                          green,
                          y_displace = -100,
                          size="large")
        # the parameter size default is small.
        message_to_screen("The objective of the game is to eat red apples",
                          black,
                          -30)

        message_to_screen("The more apples you eat, the longer you get",
                          black,
                          10)

        message_to_screen("If you run into yourself, or the edges, you die!",
                          black,
                          50)

        message_to_screen("Press C to play or Q to quit.",
                          black,
                          180)

        pygame.display.update()
        #The parameter is frame/second. The higher number the quicker response at the user input.
        clock.tick(15)


#Function to create the snake.
def snake(block_size, snakeList):

    if direction == "right":
        #Rotates the snakehead image 270 degrees.
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        #Rotates the snakehead image 270 degrees.
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        #Rotates the snakehead image 270 degrees.
        head = img

    if direction == "down":
        #Rotates the snakehead image 270 degrees.
        head = pygame.transform.rotate(img, 180)


    # Add the snakehead img to the gamedisplay. snakeList[-1][0] is the last element in the list and the X value,
    # snakeList[-1][1] is the last element in the list and the Y value,
    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))

    # Loop through all the snakelist except the last element which is the snakehead.
    for XandY in snakeList[:-1]:
        # Parameters are, where to draw it, which color, size
        pygame.draw.rect(gameDisplay, green, [XandY[0], XandY[1], block_size, block_size])

#Function that create the text Surface and return two values.
def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


# Function to write out message to the user. The function has two parameter default, y_displace parameter that
#decide where the text should be displayed. Size is the font size.
def message_to_screen(message, color, y_displace=0, size="small"):
    ''' Old version. The text does not get centered.
    screen_text = font.render(message, True, color)
    # the blit function takes the parameters and add them to the screen.
    gameDisplay.blit(screen_text, [display_width/2,display_height/2])
    '''
    #The new version get the text centered by using the textRect.
    # Get the values to the textSurface and textRect.
    textSurface, textRect = text_objects(message,color,size)
    textRect.center = (display_width/2), (display_height/2) + y_displace
    # the blit function takes the parameters and add them to the screen.
    gameDisplay.blit(textSurface, textRect)



#------------------------ gameLoop Function -----------------------------#
def gameLoop():
    # Global the variable to modify the variable direction that is using to change the snakehead image.
    global direction

    # Need to rotate the snakehead image so it start right from the beginning.
    direction = "right"

    gameExit = False
    gameOver = False

    # The leader of group of the blocks that is the snake. Head of the snake.
    lead_x = display_width / 2
    lead_y = display_height / 2

    # Variable to success when you press down a key the snake continues forward.
    lead_x_change = 10
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

            #If the function has a default parameter it is recommended to write out the variable name so it easier to get
            # understanding of the code.
            message_to_screen("Game over",
                              red,
                              y_displace=-50,
                              size="large")

            message_to_screen( "Press C to play again or Q to quit",
                               black,
                               50,
                               "medium")

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

        # ----------------------Logic for the movement---------------------------------------------------#
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:

                    # change the value of the variable so we can rotate the snakehead image.
                    direction = "left"
                    #lead_x -= 10
                    lead_x_change = -block_size
                    #We need to change y also so we dont get the snake to run diagonal.
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    #lead_x += 10
                    lead_x_change = block_size
                    lead_y_change = 0

                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    # We need to change x also so we dont get the snake to run diagonal.
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
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
        # Old version that the apple is a rectangle.
        # pygame.draw.rect(gameDisplay, red, [randAppleX,randAppleY, applethickness,applethickness])

        # Put out the apple image to the screen.
        #gameDisplay.blit(appleimg, (randAppleX, randAppleY))

        #Put out a frog image to the screen.
        #gameDisplay.blit(frogimg, (randAppleX, randAppleY))

        #Put out a pacman image to the screen.
        gameDisplay.blit(pacmanimg, (randAppleX, randAppleY))

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

game_intro()
gameLoop()