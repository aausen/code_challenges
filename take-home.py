"""A library for drawing ASCII graphics"""

class Canvas():

    def __init__(self):
        self.heigth = 10
        self.width = 10

    def print_canvas(self, shape):
        print(self, shape)

    def create_rectangle(self, height, width):
        self.char = "+"
        self.height = height
        self.width = width


    def clear_all_shapes(self):
        pass
    
    def draw_rectangle(self, x, y):
        pass
        self.start_x = x
        self.start_y = y
        # self.end_x =
        # self.end_y =

    def change_fill(self, char):
        self.create_rectangle.char = char

    def translate(self, x, y):
        pass
        
# give canvas specific height and width

# render a canvas with a specified height and width
# print the canvas and any shapes to standard input
# add a shape to the canvas 
#   for now only rectangles
# clear all shapes from the canvas
# create a rectagle
#   start_x upper left
#   start_y upper left
#   end_x lower right
#   end_y lower-right
# change a rectagle's fill character