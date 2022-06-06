from math import *

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def cart(self):
        return [self.x,self.y]

    def polaire(self):
        r = sqrt(self.x**2 + self.y**2)
        t = 2*atan(self.y/(self.x + r))
        return [r,t]
    
    def __str__(self):
        return 'x = {} \ny = {}'.format(self.x, self.y)

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    def homothétie(self,k):
        self.x = k*self.x
        self.y = k*self.y

    def translation(self,dx,dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def rotation(self,a):
        r = self.polaire()[0]
        t = self.polaire()[1]
        self.x = r*cos(t+a)
        self.y = r*sin(t+a)


if __name__ == '__main__':
    p = Point(1,0)
    q = Point(3,2)
    p.rotation(pi)
    print(p)