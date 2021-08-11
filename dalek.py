# Daleks: Escape!

# Daleks is a turn based game, played on a 2D grid. 

# Your character is being chased by multiple Daleks. You must outwit their simple programming to cause them to crash into each other. 

# Let's build it!

# https://macintoshgarden.org/sites/macintoshgarden.org/files/screenshots/NewDaleks.png
    
    
# Step 1:
# Draw a 32 column, 20 row grid to the screen. 
# A period, "." is a good character to use to represent an empty cell.

# Step 2:
# Place your character in a random position on the grid. 

# An "@" or unicode smiley "☺", are a good characters to use to represent your character.

# Step 3:

# Add a game loop. 

# Allow user input that will move your character, one step in any direction.

# Step 4:
# Add 5 Daleks! Place them in random locations. 

# A D or an unicode snowman "☃", are a good characters to use.

# ................................
# ...☃............................
# ................................
# ................................
# .............☺.......☃..........
# ................................
# ................................
# ................................
# ........☃.......................
# ....................☃...........
# ................................
# ................................
# ...................☃............
# ................................
# ................................
# ................................
# ................................
# ................................
# ................................
# ................................


# https://www.programiz.com/python-programming/global-keyword
# print('mal', end='')
import random

character_position = (random.randint(0, 19), random.randint(0, 31))
daleks = []

def create_dalek():
    global daleks
    
    for i in range(5):
        daleks.append( (random.randint(0, 19), random.randint(0, 31)) )

def draw_grid():
    for row in range(20):
        for col in range(32):
            # https://www.programiz.com/python-programming/methods/built-in/any
            
            
            
            # any((dalek == (row, col)) for dalek in daleks))
            
            has_dalek = False
            for dalek in daleks:
                if ((row, col) == dalek):
                    has_dalek = True
            
            if (row, col) == character_position:
                print("@", end="")
            elif has_dalek:
                print("D", end="")
            else:
                print(".", end="")
        print('') # print newline
    print('') # print newline
    
def move_character(direction):
    global character_position
    
    row = character_position[0]
    col = character_position[1]
    if direction == "left":
        character_position = (row, (col - 1))
    elif direction == "right":
        character_position = (row, (col + 1))
    elif direction == "up":
        character_position = ((row - 1), col)
    elif direction == "down":
        character_position = ((row + 1), col)

create_dalek()
print(daleks)
        
draw_grid()
# move_character('left')
# draw_grid()
# move_character('down')
# draw_grid()