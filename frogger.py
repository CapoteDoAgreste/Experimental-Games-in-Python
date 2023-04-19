import sys
import pygame
import random


# Set the starting position of the rectangle
initialX = 7*32+8
initialY = 12*32+4
rect_x = initialX
rect_y = initialY
player_x = initialX
player_y = initialY
coliding = False
playerSpd = 0.5
alive = True
direction = 'none'
walking = False
newPosition = 0
distance = 0
xC = 0
yC = 0
Score = 0
reset = True


def lerp(a, b, t):
    return (1 - t) * a + t * b


def round_to_multiple_of_32(num):
    return round(num / 32) * 32


def ScorePoint(x, y, w):
    xC = int(x / 32)
    yC = int(y / 32)
    try:
        if map_layout[yC][xC] == 5:
            try:
                print(
                    w.index({'x': xC*32+4, 'y': 4, 'color': (94, 235, 52)}))
                print('Already exist a point in the place')
            except:
                print('adding')
                w.append({'x': xC*32+4, 'y': 4, 'color': (94, 235, 52)})
                print(Score+1)
            return True
        else:
            return False
    except:
        return False


def inWater(x, y, obj):
    # getting player position on map layout
    xC = int(x / 32)
    yC = int(y / 32)
    isSafePlace = False

    # verifying if the player is on the water and if he is above a object
    try:
        if map_layout[yC][xC] == 3 or map_layout[yC][xC] == 4:
            for oObj in obj:
                for nObj in oObj:
                    if y + 24 >= nObj['y'] and y <= nObj['y'] + 24:
                        if x + 24 >= nObj['x'] and x <= nObj['x'] + 24:
                            isSafePlace = True
        else:
            return False

        if isSafePlace == False:
            return True
        else:
            return False
    except:
        return False


def addMovement(obj):
    obj['x'] += obj['direction']
    if obj['direction'] > 0 and obj['x'] > 16*32:
        obj['x'] = -32
    if log['direction'] < 0 and obj['x'] < -32:
        obj['x'] = 16*32


# Initialize Pygame
pygame.init()

# Set the window size
window_size = (15*32, 13*32)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("A Frogger Clone")

# Set up the game clock
clock = pygame.time.Clock()

font = pygame.font.SysFont("comicsansms", 24)

map_layout = [
    [4, 5, 4, 4, 5, 4, 4, 5, 4, 4, 5, 4, 4, 5, 4],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
]

'''
map_layout was maked with that symbols and meanings
0 - street
1 - null
2 - sidewalk
3 - water
4 - grass
5 - Score Point
'''


# Define the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 102, 102)
green = (182, 255, 93)
drkGreen = (28, 166, 19)
brown = (188, 132, 29)
violet = (185, 126, 251)
pink = (251, 126, 232)
blue = (0, 128, 255)
lightBlue = (153, 255, 255)
yellow = (255, 255, 153)
orange = (255, 178, 153)
lightGreen = (237, 253, 196)
frog = (94, 235, 52)

# defining cars
cars = [

    # line 12
    {
        'x': 8,
        'y': 32*11,
        'direction': 1,
        'color': yellow
    },
    {
        'x': 32*4+8,
        'y': 32*11,
        'direction': 1,
        'color': yellow
    },
    {
        'x': 32*8+8,
        'y': 32*11,
        'direction': 1,
        'color': yellow
    },
    {
        'x': 32*12+8,
        'y': 32*11,
        'direction': 1,
        'color': yellow
    },

    # line 11

    {
        'x': 0+8,
        'y': 32*10,
        'direction': -1,
        'color': lightBlue
    },
    {
        'x': 32*4+8,
        'y': 32*10,
        'direction': -1,
        'color': lightBlue
    },
    {
        'x': 32*8+8,
        'y': 32*10,
        'direction': -1,
        'color': lightBlue
    },
    {
        'x': 32*12+8,
        'y': 32*10,
        'direction': -1,
        'color': lightBlue
    },

    # line 10

    {
        'x': 0+8,
        'y': 32*9,
        'direction': 1,
        'color': pink
    },
    {
        'x': 32*4+8,
        'y': 32*9,
        'direction': 1,
        'color': pink
    },
    {
        'x': 32*8+8,
        'y': 32*9,
        'direction': 1,
        'color': pink
    },
    {
        'x': 32*12+8,
        'y': 32*9,
        'direction': 1,
        'color': pink
    },

    # line 8

    {
        'x': 0+8,
        'y': 32*8,
        'direction': 3,
        'color': red
    },
    {
        'x': 32*4+8,
        'y': 32*8,
        'direction': 3,
        'color': red
    },

    # line 7

    {
        'x': 0+8,
        'y': 32*7,
        'direction': -0.5,
        'color': white
    },
    {
        'x': 32+8,
        'y': 32*7,
        'direction': -0.5,
        'color': white
    },
    {
        'x': 32*5+8,
        'y': 32*7,
        'direction': -0.5,
        'color': white
    },
    {
        'x': 32*6+8,
        'y': 32*7,
        'direction': -0.5,
        'color': white
    },
    {
        'x': 32*10+8,
        'y': 32*7,
        'direction': -0.5,
        'color': white
    },
    {
        'x': 32*11+8,
        'y': 32*7,
        'direction': -0.5,
        'color': white
    }
]
# defining turtles
turtles = [
    # line 6
    {
        'x': 32*0+8,
        'y': 32*5,
        'direction': -1,
        'color': drkGreen
    },
    {
        'x': 32*1+8,
        'y': 32*5,
        'direction': -1,
        'color': drkGreen
    },
    {
        'x': 32*2+8,
        'y': 32*5,
        'direction': -1,
        'color': drkGreen
    },
    {
        'x': 32*4+8,
        'y': 32*5,
        'direction': -1,
        'color': lightGreen
    },
    {
        'x': 32*5+8,
        'y': 32*5,
        'direction': -1,
        'color': lightGreen
    },
    {
        'x': 32*6+8,
        'y': 32*5,
        'direction': -1,
        'color': lightGreen
    },
    {
        'x': 32*8+8,
        'y': 32*5,
        'direction': -1,
        'color': drkGreen
    },
    {
        'x': 32*9+8,
        'y': 32*5,
        'direction': -1,
        'color': drkGreen
    },
    {
        'x': 32*10+8,
        'y': 32*5,
        'direction': -1,
        'color': drkGreen
    },
    # line 3
    {
        'x': 32*0,
        'y': 32*2,
        'direction': -1,
        'color': lightGreen
    },
    {
        'x': 32*1,
        'y': 32*2,
        'direction': -1,
        'color': lightGreen
    },
    {
        'x': 32*3,
        'y': 32*2,
        'direction': -1,
        'color': drkGreen
    },
    {
        'x': 32*4,
        'y': 32*2,
        'direction': -1,
        'color': drkGreen
    },
    {
        'x': 32*8,
        'y': 32*2,
        'direction': -1,
        'color': drkGreen
    },
    {
        'x': 32*9,
        'y': 32*2,
        'direction': -1,
        'color': drkGreen
    },
    {
        'x': 32*11,
        'y': 32*2,
        'direction': -1,
        'color': drkGreen
    },
    {
        'x': 32*12,
        'y': 32*2,
        'direction': -1,
        'color': drkGreen
    }
]
# defining logs of wood
logs = [
    # line 5
    {
        'x': 32*0,
        'y': 32*4,
        'direction': 0.5,
        'color': brown
    },
    {
        'x': 32*1,
        'y': 32*4,
        'direction': 0.5,
        'color': brown
    },
    {
        'x': 32*2,
        'y': 32*4,
        'direction': 0.5,
        'color': brown
    },
    {
        'x': 32*5,
        'y': 32*4,
        'direction': 0.5,
        'color': brown
    },
    {
        'x': 32*6,
        'y': 32*4,
        'direction': 0.5,
        'color': brown
    },
    {
        'x': 32*7,
        'y': 32*4,
        'direction': 0.5,
        'color': brown
    },
    {
        'x': 32*10,
        'y': 32*4,
        'direction': 0.5,
        'color': brown
    },
    {
        'x': 32*11,
        'y': 32*4,
        'direction': 0.5,
        'color': brown
    },
    {
        'x': 32*12,
        'y': 32*4,
        'direction': 0.5,
        'color': brown
    },

    # line 4

    {
        'x': 32*0,
        'y': 32*3,
        'direction': 4,
        'color': brown
    },
    {
        'x': 32*1,
        'y': 32*3,
        'direction': 4,
        'color': brown
    },
    {
        'x': 32*2,
        'y': 32*3,
        'direction': 4,
        'color': brown
    },
    {
        'x': 32*3,
        'y': 32*3,
        'direction': 4,
        'color': brown
    },
    {
        'x': 32*4,
        'y': 32*3,
        'direction': 4,
        'color': brown
    },
    {
        'x': 32*5,
        'y': 32*3,
        'direction': 4,
        'color': brown
    },
    {
        'x': 32*8,
        'y': 32*3,
        'direction': 4,
        'color': brown
    },
    {
        'x': 32*9,
        'y': 32*3,
        'direction': 4,
        'color': brown
    },
    {
        'x': 32*10,
        'y': 32*3,
        'direction': 4,
        'color': brown
    },
    {
        'x': 32*11,
        'y': 32*3,
        'direction': 4,
        'color': brown
    },
    {
        'x': 32*12,
        'y': 32*3,
        'direction': 4,
        'color': brown
    },
    {
        'x': 32*13,
        'y': 32*3,
        'direction': 4,
        'color': brown
    },

    # line 2

    {
        'x': 32*0,
        'y': 32*1,
        'direction': 1,
        'color': brown
    },
    {
        'x': 32*1,
        'y': 32*1,
        'direction': 1,
        'color': brown
    },
    {
        'x': 32*2,
        'y': 32*1,
        'direction': 1,
        'color': brown
    },
    {
        'x': 32*3,
        'y': 32*1,
        'direction': 1,
        'color': brown
    },
    {
        'x': 32*6,
        'y': 32*1,
        'direction': 1,
        'color': brown
    },
    {
        'x': 32*7,
        'y': 32*1,
        'direction': 1,
        'color': brown
    },
    {
        'x': 32*8,
        'y': 32*1,
        'direction': 1,
        'color': brown
    },
    {
        'x': 32*9,
        'y': 32*1,
        'direction': 1,
        'color': brown
    },
    {
        'x': 32*12,
        'y': 32*1,
        'direction': 1,
        'color': brown
    },
    {
        'x': 32*13,
        'y': 32*1,
        'direction': 1,
        'color': brown
    },
    {
        'x': 32*14,
        'y': 32*1,
        'direction': 1,
        'color': brown
    },
    {
        'x': 32*15,
        'y': 32*1,
        'direction': 1,
        'color': brown
    }

]

winPlaces = [
    {
        'x': 32*1,
        'y': 32*1,
    },
    {
        'x': 32*4,
        'y': 32*1,
    },
    {
        'x': 32*7,
        'y': 32*1,
    },
    {
        'x': 32*10,
        'y': 32*1,
    },
    {
        'x': 32*13,
        'y': 32*1,
    }
]

wins = []

# Set the movement speed of the rectangle

# Run the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Asign keys into a variable and verifying it be pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and walking == False:
        direction = 'left'
        newPosition = rect_x - 32
        player_x -= 32
        walking = True
    if keys[pygame.K_RIGHT] and walking == False:
        direction = 'right'
        newPosition = rect_x + 32
        player_x += 32
        walking = True
    if keys[pygame.K_UP] and walking == False:
        direction = 'up'
        newPosition = rect_y - 32
        player_y -= 32
        walking = True
    if keys[pygame.K_DOWN] and walking == False:
        direction = 'down'
        newPosition = rect_y + 32
        player_y += 32
        walking = True
    if keys[pygame.K_r]:
        reset = True

    # Draw the game
    screen.fill(black)

    # to simulate a frog walk of frogger, a lerp was added, to crate a delay beetween each move.
    if walking:

        if direction == 'left' or direction == 'right':
            rect_x = lerp(rect_x, newPosition, playerSpd)
            distance = rect_x - newPosition
        if direction == 'up' or direction == 'down':
            rect_y = lerp(rect_y, newPosition, playerSpd)
            distance = rect_y - newPosition

        if distance < 0:
            distance *= -1
        if (distance < 0.001):
            walking = False
            direction = 'none'

    # drawing the tilemap accorrding to their material id
    for y in range(len(map_layout)):
        for x in range(len(map_layout[y])):
            if map_layout[y][x] == 2:
                pygame.draw.rect(screen, violet, (
                    x*32, y*32, 32, 32))
            if map_layout[y][x] == 3 or map_layout[y][x] == 5:
                pygame.draw.rect(screen, blue, (
                    x*32, y*32, 32, 32))
            if map_layout[y][x] == 4:
                pygame.draw.rect(screen, drkGreen, (
                    x*32, y*32, 32, 32))

    # adding colision and draw events into car objects
    for car in cars:
        if car['color'] != white:
            pygame.draw.rect(screen, car['color'],
                             (car['x'], car['y'], 24, 24))
        else:
            pygame.draw.rect(screen, car['color'],
                             (car['x'], car['y'], 32, 24))
        car['x'] += car['direction']
        if car['direction'] > 0 and car['x'] > 16*32:
            car['x'] = -32
        if car['direction'] < 0 and car['x'] < -32:
            car['x'] = 16*32

        if player_y + 24 >= car['y'] and player_y <= car['y'] + 24:
            if player_x + 24 >= car['x'] and player_x <= car['x'] + 24:
                walking = True
                reset = True
                print('colidiu')
    c1 = lerp(237, 255, 0.1)
    c2 = lerp(253, 255, 0.1)
    c3 = lerp(196, 255, 0.1)
    newColor = (c1, c2, c3)

    # adding colision and draw events into turtle objects
    for turtle in turtles:
        if turtle['color'] == lightGreen:
            pygame.draw.rect(screen, newColor,
                             (turtle['x'], turtle['y'], 24, 24))
        else:
            pygame.draw.rect(screen, turtle['color'],
                             (turtle['x'], turtle['y'], 24, 24))
        turtle['x'] += turtle['direction']
        if turtle['direction'] > 0 and turtle['x'] > 16*32:
            turtle['x'] = -32
        if turtle['direction'] < 0 and turtle['x'] < -32:
            turtle['x'] = 16*32

        if player_y + 24 >= turtle['y'] and player_y <= turtle['y'] + 24:
            if player_x + 24 >= turtle['x'] and player_x <= turtle['x'] + 24:
                # 123
                player_x += turtle['direction']
                # rect_x = player_x+0.0001
                coliding = True
            else:
                coliding = False

    # adding colision and draw events into log objects
    for log in logs:
        pygame.draw.rect(screen, log['color'], (log['x'], log['y'], 32, 24))
        addMovement(log)
        if player_y + 24 >= log['y'] and player_y <= log['y'] + 24:
            if player_x + 24 >= log['x'] and player_x <= log['x'] + 24:
                # 123
                player_x += log['direction']
                # rect_x = player_x+0.0001
                coliding = True
            else:
                coliding = False

    if not wins:
        None
    else:
        for win in wins:
            pygame.draw.rect(screen, log['color'],
                             (win['x'], win['y'], 24, 24))
    # Storing water object in a variable
    allObj = [logs, turtles, winPlaces]
    # verifying if the player has falled in the water

    isInWater = inWater(player_x, player_y, allObj)
    Scored = ScorePoint(player_x, player_y, wins)
    if Scored == True:
        Score += 1
        print(wins)
        print(Score)
        reset = True
    if isInWater == True:
        reset = True
    if reset == True:
        rect_x = initialX
        rect_y = initialY
        player_x = rect_x
        player_y = rect_y
        walking = False
        reset = False

    # Drawing the player on the screen
    pygame.draw.rect(screen, frog, (player_x, player_y, 24, 24))
    # Update the window
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)
