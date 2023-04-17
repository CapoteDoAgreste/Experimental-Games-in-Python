import sys
import pygame
import random


def lerp(a, b, t):
    return (1 - t) * a + t * b


# Set the initial angle and target angle
angle = 0
target_angle = -75


# Initialize Pygame
pygame.init()

# Set the window size
width = 640
height = 480
window_size = (width, height)
playerImages = ['sprite_0', 'sprite_1', 'sprite_2',
                'sprite_3', 'sprite_4', 'sprite_5', 'sprite_6', 'sprite_7']
frameIndex = 0

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Flappy Bird Clone")

# Set up the game clock
clock = pygame.time.Clock()

font = pygame.font.SysFont("comicsansms", 24)


# Define the colors
black = (132, 200, 249)
white = (255, 255, 255)
green = (150, 255, 0)

# Set the starting position of the rectangle
rect_x = width/2-25
rect_y = height/2-25

# Setting Alive Variable
alive = True

# Set the movement speed of the rectangle
rect_speed = 5

# Set the initial score
score = 0

# Setting initial cans
cans = [

    {
        'x': width+300,
        'y': -200,
        'position': 'top'
    },
    {
        'x': width+300,
        'y': 250,
        'position': 'bottom'
    },
    {
        'x': width+600,
        'y': -100,
        'position': 'top'
    },
    {
        'x': width+600,
        'y': 350,
        'position': 'bottom'
    },
    {
        'x': width+900,
        'y': -250,
        'position': 'top'
    },
    {
        'x': width+900,
        'y': 200,
        'position': 'bottom'
    }
]

# set log size
canSizeX = 60
canSizeY = 300
log_spd = 3
gravity = 0.1
coliding = False
vertical_speed = 0
canY = 0

# Run the game loop
while True:
    text_surface = font.render("Score: "+str(score), True, (255, 255, 255))
    text_pos = text_surface.get_rect(center=(60, 40))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the game state
    keys = pygame.key.get_pressed()
    if alive == True:
        if keys[pygame.K_UP]:
            # Apply an upward force to the player when the up arrow is pressed
            frameIndex = 4
            vertical_speed = -3
            angle = lerp(angle, 0, 0.5)
    if keys[pygame.K_r]:
        # "R" is de reset game key
        # Resetting variables
        score = 0

        cans = [

            {
                'x': width+300,
                'y': -200,
                'position': 'top'
            },
            {
                'x': width+300,
                'y': 250,
                'position': 'bottom'
            },
            {
                'x': width+600,
                'y': -100,
                'position': 'top'
            },
            {
                'x': width+600,
                'y': 350,
                'position': 'bottom'
            },
            {
                'x': width+900,
                'y': -250,
                'position': 'top'
            },
            {
                'x': width+900,
                'y': 200,
                'position': 'bottom'
            }
        ]
        alive = True
        rect_x = width/2-25
        rect_y = height/2-25
        canSizeX = 60
        canSizeY = 300
        log_spd = 3
        gravity = 0.1
        coliding = False
        vertical_speed = 0

    # Apply gravity to the player's vertical speed
    vertical_speed += gravity

    # Draw the game
    screen.fill(black)
    frameIndex += 0.1
    for can in cans:
        # Drawing cans on the screen
        pygame.image
        pygame.draw.rect(
            screen, green, (can['x'], can['y'], canSizeX, canSizeY))

        # Cans collision
        pygame.draw.rect(
            screen, white, (rect_x+4, rect_y+8, 32+8, 32-8))
        if rect_y+8 + 32-8 >= can['y'] and rect_y+8 <= can['y'] + canSizeY:
            if rect_x + 32-8 >= can['x'] and rect_x <= can['x'] + canSizeX:
                alive = False

        if alive == True:
            # Reseting can who the player already avoided
            if can['x'] < -60:
                can['x'] = width+300
                if can['position'] == 'top':
                    can['y'] = random.randint(30-canSizeY, 300-canSizeY)
                    canY = can['y']
                else:
                    can['y'] = canY + canSizeY + 150
            if can['x'] == rect_x-1:
                # Inscreasing score
                score += 0.5
            # Making the can move into the player direction
            can['x'] -= 2

    # Drawing player on the screen
    if frameIndex > 7:
        frameIndex = 0
    image = pygame.image.load(
        "images/"+playerImages[int(frameIndex)]+'.png')

    angle = lerp(angle, target_angle, 0.008)
    rotated_image = pygame.transform.rotate(image, angle)
    screen.blit(rotated_image, (rect_x, rect_y))
    # Making the player be affected by gravity
    rect_y += vertical_speed

    # Killing the player when he hit the ground
    if rect_y > 480:
        alive = False

    # Drawing Score on the Screen

    screen.blit(text_surface, text_pos)
    # Update the window
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)
