"""A library for drawing ASCII graphics"""

# create a class for canvas
class Canvas():
    height = 100
    width = 100

    def print_canvas(self):
        print()

    def create_rectangle(self, height, width):
        self.height = height
        self.width = width


    def clear_all_shapes(self):
        pass
    
    def draw_rectangle(self):
        pass
        # self.start_x = 
        # self.start_y =
        # self.end_x =
        # self.end_y =

    def change_fill(self):
        pass

    def translate(self):
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