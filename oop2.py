class square():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def square_area(self):
        return self.length*self.width
    
newSquare = square(10, 10)
print("Dimension of square - length : %d width : %d" % (newsquare.length,newRectangle.width))
print("Area of square :", newSquare.square_area())