class Rectangle:
    def __init__(self, width, height, c):
        self.width = width
        self.height = height
        self.c = c
    def perimeter(self):
        return 2 * (self.width + self.height)
    def area(self):
        return self.width * self.height
    def color(self):
        c = self.c
        return c[0].upper() + c[1:].lower()
    
a = input().split()
if int(a[0]) > 0 and int(a[1]) > 0:
    r = Rectangle(int(a[0]), int(a[1]), a[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print("INVALID")