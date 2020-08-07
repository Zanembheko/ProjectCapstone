import pygame # import function to create pygame
import random # inport function to create random numbers

# to initilize the pygame 
pygame.init()

# creating screen and setting its width and length
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

# create a speed which will be 1 pixel
vel = 1

# create a caption to name the game
pygame.display.set_caption("Zano's First Game")

# load all images that will be used in the game
player = pygame.image.load("image.png")
enemy1 = pygame.image.load("enemy.png")
enemy2 = pygame.image.load("monster.jpg")
enemy3 = pygame.image.load("player.jpg")
win_image = pygame.image.load("prize.jpg")

# create boundaries for the image to ensure that they remain in the bounds of the screen
image_height = player.get_height()
image_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy3.get_height()
enemy2_width = enemy3.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

# creating x and y postion for player 
playerXPosition = 0
playerYPosition = 400

# Creating x and y position for enemy
# all enemies will appear at random y position
enemy1XPosition =  800
enemy1YPosition =  random.randint(0, screen_height - enemy1_height)
enemy2XPosition =  700
enemy2YPosition =  random.randint(0, screen_height - enemy2_height)
enemy3XPosition =  650
enemy3YPosition =  random.randint(0, screen_height - enemy3_height)


# create a bloolean play to remain true 
play = True

# while the play is true then it should continue running
while play:
# create the screen colour
    screen.fill((150, 220, 100))
# if the user press the quit button then the game will exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

# function to draw images of the player and enemies according to positions created 
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))

# following code will test if the keys are pressed and then move the image of the player as per instruction
    button = pygame.key.get_pressed()
# create and allow player to move to the left
    if button[pygame.K_LEFT] and playerXPosition > vel:
        playerXPosition -= vel
# create and allow player to move to the right
    if button[pygame.K_RIGHT] and playerXPosition < 800 - 100 - vel:
        playerXPosition += vel
# create and allow player to move to the up
    if button[pygame.K_UP] and playerYPosition > vel:
        playerYPosition -= vel
# create and allow player to move to the down
    if button[pygame.K_DOWN] and playerYPosition < 800 - 100 - vel:
        playerYPosition += vel


    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemy:
    
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition
    # Test collision of the boxes:
    
    if playerBox.colliderect(enemy1Box) or playerBox.colliderect(enemy2Box) or playerBox.colliderect(enemy3Box):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)

    if enemy1XPosition < 0 - enemy1_width and enemy2XPosition < 0 - enemy2_width and enemy3XPosition < 0 - enemy3_width:
    
        # Display wining status to the user:
        # Display the prize image
        screen.blit(win_image, (400, 400))
        
        pygame.display.update()
        print("You win!")
        
        
        # Quit game and exit window: 
        pygame.quit()
        
        exit(0)
    enemy1XPosition -= 0.35
    enemy2XPosition -= 0.25
    enemy3XPosition -= 0.15
   # screen.fill((0, 0, 0))
        
    pygame.display.update()
pygame.quit()    
