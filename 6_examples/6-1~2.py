class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x
    
    def sety(self, y):
        self.y = y

    def get(self):
        return (self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

point = Point(11, 2)
print(point.get())
point.setx(3)
print(point.get())
point.sety(12)
print(point.get())
point.move(2, 3)
print(point.get())