class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # Write your code here
    def change_position(self,x,y):
        self.x=x
        self.y=y
    def get_position(self):
        position = (self.x,self.y)
        return position
    def get_area(self):
        return self.width * self.height
