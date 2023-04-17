import sys
import pygame
import random


def lerp(a, b, t):
    return (1 - t) * a + t * b


def addSnakePart():
    lastIndex = len(snakeBody)-1
    match(direction):
        case 'left':
            newPartX = snakeBody[lastIndex]['x']+32
            newPartY = snakeBody[lastIndex]['y']
        case 'right':
            newPartX = snakeBody[lastIndex]['x']-32
            newPartY = snakeBody[lastIndex]['y']
        case 'up':
            newPartX = snakeBody[lastIndex]['x']
            newPartY = snakeBody[lastIndex]['y']+32
        case 'down':
            newPartX = snakeBody[lastIndex]['x']
            newPartY = snakeBody[lastIndex]['y']-32
    snakeBody.append({'x': newPartX, 'y': newPartY})


def resetGame():
    rect_x = 200
    rect_y = 200
    log_spd = 3
    gravity = 0.1
    coliding = False
    score = 0
    alive = True
    snakeBody = [

        {
            'x': 232,
            'y': 200
        },
        {
            'x': 264,
            'y': 200
        },
        {
            'x': 296,
            'y': 200
        }
    ]


# Initialize Pygame
pygame.init()

# Set the window size
window_size = (640, 480)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Zen Snake")

# Set up the game clock
clock = pygame.time.Clock()

font = pygame.font.SysFont("comicsansms", 24)


# Define the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (150, 75, 0)

# Set the starting position of the rectangle
rect_x = 200
rect_y = 200
alive = True

apple = {
    'x': random.randint(32, 608),
    'y': random.randint(32, 480-32)
}

snakeBody = [

    {
        'x': 232,
        'y': 200
    },
    {
        'x': 264,
        'y': 200
    },
    {
        'x': 296,
        'y': 200
    }
]

# Set the movement speed of the rectangle
rect_speed = 5
direction = 'left'
score = 0
coliding = False

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
    if keys[pygame.K_LEFT] and direction != 'right':
        direction = 'left'
    if keys[pygame.K_RIGHT] and direction != 'left':
        direction = 'right'
    if keys[pygame.K_UP] and direction != 'down':
        direction = 'up'
    if keys[pygame.K_DOWN] and direction != 'up':
        direction = 'down'
    if keys[pygame.K_z]:
        addSnakePart()
    if keys[pygame.K_r]:
        snakeBody = [

            {
                'x': 232,
                'y': 200
            },
            {
                'x': 264,
                'y': 200
            },
            {
                'x': 296,
                'y': 200
            }
        ]
        direction = 'left'
        score = 0
        rect_x = 200
        rect_y = 200
        apple = {
            'x': random.randint(32, 608),
            'y': random.randint(32, 480-32)
        }

    # Draw the game
    screen.fill(black)

    match(direction):
        case 'left':
            rect_x -= rect_speed
        case 'right':
            rect_x += rect_speed
        case 'up':
            rect_y -= rect_speed
        case 'down':
            rect_y += rect_speed

    pygame.draw.rect(screen, white, (rect_x, rect_y, 32, 32))
    for part in snakeBody:
        if part['x'] == snakeBody[0]['x'] and part['y'] == snakeBody[0]['y']:
            part['x'] = lerp(part['x'], rect_x, 0.1)
            part['y'] = lerp(part['y'], rect_y, 0.1)
            if rect_y + 32 >= apple['y'] and rect_y <= apple['y'] + 32:
                if rect_x + 32 >= apple['x'] and rect_x <= apple['x'] + 32:
                    apple['x'] = random.randint(32, 608)
                    apple['y'] = random.randint(32, 480-32)
                    addSnakePart()
                    score += 1
        else:
            index = snakeBody.index(part)-1
            part['x'] = lerp(part['x'], snakeBody[index]['x'], 0.1)
            part['y'] = lerp(part['y'], snakeBody[index]['y'], 0.1)

        pygame.draw.rect(screen, red, (apple['x'], apple['y'], 32, 32))
        pygame.draw.rect(screen, white, (part['x'], part['y'], 32, 32))

    screen.blit(text_surface, text_pos)
    # Update the window
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)
