"""A library for drawing ASCII graphics"""

class Canvas():

    def __init__(self):
        self.heigth = 10
        self.width = 10
        # canvas = []

    def print_canvas(self, shape):
        pass

    def create_rectangle(self, height, width):
        self.height = height
        self.width = width


    def clear_all_shapes(self):
        pass
    
class Rectangle(Canvas):

    def draw_rectangle(self, start_x, start_y, end_x, end_y, fill_char):
        start_x = start_x
        start_y = start_y
        end_x = end_x
        end_y = end_y
        fill_char = fill_char

        return print(fill_char(start_x * end_x))

    def change_fill(self, char):
        self.create_rectangle.fill_char = char

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