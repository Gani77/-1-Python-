from math import sqrt

class Triangle():
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.lenVector = {
                'a': round(sqrt((self.point1[0] - self.point2[0]) ** 2 + (self.point1[1] - self.point2[1]) ** 2), 2),
                'b': round(sqrt((self.point2[0] - self.point3[0]) ** 2 + (self.point2[1] - self.point3[1]) ** 2), 2),
                'c': round(sqrt((self.point1[0] - self.point3[0]) ** 2 + (self.point1[1] - self.point3[1]) ** 2), 2)
                }

    def Height(self):
        p = 1 / 2 * (self.lenVector['a'] + self.lenVector['b'] + self.lenVector['c'])
        return round((2 * sqrt(p * (p - self.lenVector['a']) * (p - self.lenVector['b']) * (p - self.lenVector['c']))) / self.lenVector['a'], 2)
    def Square(self):
        return round(1 / 2 * self.lenVector['a'] * self.Height(), 2)
    def Perimetr(self):
        return self.lenVector['a'] + self.lenVector['b'] + self.lenVector['c']

#снизу все для проверки 
#test = Triangle((0, 0), (4, 4), (4, 0)) 
#print(test.Perimetr())
#print(test.Height())
#print(test.Square())
