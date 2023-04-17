import sys
import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (640, 480)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Rectangle Game")

# Set up the game clock
clock = pygame.time.Clock()

font = pygame.font.SysFont("comicsansms", 24)


# Define the colors
black = (0, 0, 0)
white = (255, 255, 255)
brown = (150, 75, 0)

# Set the starting position of the rectangle
rect_x = 200
rect_y = 200
alive = True

# Set the movement speed of the rectangle
rect_speed = 5

score = 0

logs = [

    {
        'x': -300,
        'y': 50
    },
    {
        'x': -100,
        'y': 250
    },
    {
        'x': 200,
        'y': 400
    }
]

# set log size
logSizeX = 200
logSizeY = 40
log_spd = 3
gravity = 0.1
coliding = False
vertical_speed = 0

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
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        # Apply an upward force to the player when the up arrow is pressed
        if (coliding == True):
            vertical_speed = -5
            if (coliding == True):
                rect_y += vertical_speed
                coliding = False
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed
    if keys[pygame.K_r]:
        logs = [

            {
                'x': -300,
                'y': 50
            },
            {
                'x': -100,
                'y': 250
            },
            {
                'x': 200,
                'y': 400
            }
        ]
        rect_x = 200
        rect_y = 200
        log_spd = 3
        gravity = 0.1
        coliding = False
        vertical_speed = 0
        score = 0
        alive = True

    # Apply gravity to the player's vertical speed
    vertical_speed += gravity

    # Draw the game
    screen.fill(black)

    pygame.draw.rect(screen, white, (rect_x, rect_y, 50, 50))

    for log in logs:
        pygame.draw.rect(
            screen, brown, (log['x'], log['y'], logSizeX, logSizeY))

        log['x'] += log_spd

        if log['x'] >= 640:
            log['x'] = -200
            log['y'] = random.randint(30, 450)
            if (log_spd <= 11):
                log_spd += log_spd*0.1
            if (alive == True):
                score += 1

        if rect_y + 50 >= log['y'] and rect_y <= log['y'] + logSizeY:
            if rect_x + 50 >= log['x'] and rect_x <= log['x'] + logSizeX:
                # The player has collided with a log, reset their position
                coliding = True
            else:
                coliding = False

    if coliding == True:
        rect_x += log_spd
        vertical_speed = 0
    else:
        # Update the player's position based on their vertical speed
        rect_y += vertical_speed
    if rect_y > 480:
        alive = False

    screen.blit(text_surface, text_pos)
    # Update the window
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)
