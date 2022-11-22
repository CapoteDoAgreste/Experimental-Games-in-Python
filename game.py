from time import sleep as s
import random
import arcade

# Set how many rows and columns we will have
ROW_COUNT = 15
COLUMN_COUNT = 15

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "Array Backed Grid Example"

class Game:
    score = 0
    game_over = False

class Player:
    dir = 1
    body = [[6,1],[5,1],[4,1],[3,1]]
    locBody = [] 
    initLocation = [[6,1],[5,1],[4,1],[3,1]]

class Apple:
    x = 1
    y = 1
    onMap = False





class MyGame(arcade.Window):
    """
    Main application class.
    """

    def _init_(self, width, height, title):
        """
        Set up the application.
        """

        super()._init_(width, height, title)

        # Create a 2 dimensional array. A two-dimensional
        # array is simply a list of lists.
        self.grid = []
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)  # Append a cell

        arcade.set_background_color(arcade.color.BLACK)


    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        start_x = 10
        start_y = 500
        arcade.draw_text("Score:" + str(Game.score),
                         start_x,
                         start_y,
                         arcade.color.WARM_BLACK,
                         20, bold=True)

        self.grid = []

        #Clear the screen to show the next frame
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)  # Append a cell

        #Render game objects
        self.grid[Apple.y][Apple.x] = 2
        #SnakeBody
        for i in range(0,len(Player.body)):
            self.grid[Player.body[i][1]][Player.body[i][0]] = 1
        #Snake head
        self.grid[Player.body[0][1]][Player.body[0][0]] = 3

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # Figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                elif self.grid[row][column] == 2:
                    color = arcade.color.RED
                elif self.grid[row][column] == 3:
                    color = arcade.color.DARK_GREEN
                else:
                    color = arcade.color.WHITE

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)


    def on_update(self, delta_time):
        '''
        dir 
        0 = left
        1 = right
        2 = down
        3 = up
        '''

        
        #Move the player

        match(Player.dir):
            case 0:
                if(Player.body[0][0]-1 >= 0):
                    Player.body[0][0]-=1
                else:
                    Game.game_over = True
            case 1:
                if(Player.body[0][0]+1 < ROW_COUNT):
                    Player.body[0][0]+=1
                else:
                    Game.game_over = True
            case 2:
                if(Player.body[0][1]-1 >= 0):
                    Player.body[0][1]-=1
                else:
                    Game.game_over = True
            case 3:
                if(Player.body[0][1]+1 < COLUMN_COUNT):
                    Player.body[0][1]+=1
                else:
                    Game.game_over = True

        #previous snake parts location
        Player.locBody = list(Player.body)
                    
        for i in range(len(Player.body)-1,0,-1):
            if(Player.body[i][0]!=Player.locBody[i-1][0] or Player.body[i][1]!=Player.locBody[i-1][1]):
                Player.body[i][0] = Player.body[i-1][0]
                Player.body[i][1] = Player.body[i-1][1]
    

        #init apple and create another one when eated
        if(Apple.onMap == False):
            size = len(Player.body)
            Player.body.append([])
            Player.body[size].append(0)
            Player.body[size].append(0)
            Apple.x = random.randint(2,ROW_COUNT-2)
            Apple.y = random.randint(2,ROW_COUNT-2)
            Apple.onMap = True
            print("x ",Apple.x,"y ",Apple.y)


        #Eat init trigger
        if(Player.body[0][0] == Apple.x and Player.body[0][1] == Apple.y):
            Apple.onMap = False
            Game.score += 1

        '''
        for i in range(len(Player.body)-1,0,-1):
            if(Player.body[0][0] == Player.body[i][0] and Player.body[0][1] == Player.body[i][1]):
                Game.game_over = True
        '''

        if(Game.game_over == True):
            Game.game_over = False
            Player.body = list(Player.initLocation)
            Player.dir = 1
            Game.score = 0
            Apple.onMap = False

    def on_key_press(self, key, modifiers):

        #Keyboard commands and actions
        up = arcade.key.UP
        down = arcade.key.DOWN
        left = arcade.key.LEFT
        right = arcade.key.RIGHT

        if (key in [up,down,left,right]):
            if (key == up and Player.dir != 2):
                Player.dir = 3
            if (key == down and Player.dir != 3):
                Player.dir = 2
            if (key == left and Player.dir != 1):
                Player.dir = 0
            if (key == right and Player.dir != 0):
                Player.dir = 1

    

def main():

    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()