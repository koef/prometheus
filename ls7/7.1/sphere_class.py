# -*- coding: utf-8 -*-
__author__ = 'koef'
from math import pi
from math import sqrt

class Sphere(object):
    def __init__(self, radius = 1.0, x=0.0, y=0.0, z=0.0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return 4.0/3 * pi * self.radius ** 3

    def get_square(self):
        return 4.0 * pi * self.radius ** 2

    def get_radius(self):
        return float(self.radius)

    def get_center(self):
        return float(self.x), float(self.y), float(self.z)

    def set_radius(self, r):
        self.radius = r

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        ab = abs(sqrt((x-self.x)**2+(y-self.y)**2+(z-self.z)**2))
        if ab < self.radius:
            return True
        else:
            return False


sp1 = Sphere(1.99, 1, 2, -1)
print("Радиус: %s" % (sp1.get_radius()))
print("Объем сферы: %s" % (sp1.get_volume()))
print("Площадь сферы: %s" % (sp1.get_square()))
print("Координаты центра: %s" % (str(sp1.get_center())))
print("Находится ли %s точка внутри сферы: %s" % ("0, 0, 0.99", sp1.is_point_inside(0, 0, 0.99)))
print("__________________")
print

sp1.set_radius(2)
sp1.set_center(0, 0, 0)
print("Радиус: %s" % (sp1.get_radius()))
print("Объем сферы: %s" % (sp1.get_volume()))
print("Площадь сферы: %s" % (sp1.get_square()))
print("Координаты центра: %s" % (str(sp1.get_center())))
print("Находится ли %s точка внутри сферы: %s" % ("0, 0, 2.99", sp1.is_point_inside(0, 0, 2.99)))

