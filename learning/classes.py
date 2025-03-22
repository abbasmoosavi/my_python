class Point:
    def move(self):
        print('Move')
    def draw(self):
        print('Draw')
        
point1 = Point()
point1.draw()

point1.x = 20
point1.y =10

print(point1.x)
# Draw
# 20