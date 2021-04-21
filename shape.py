import math

def circle_area(radius):
    """ returns the area of a circle """
    # Area is pi * r squared
    area = math.pi * radius * radius
    return area 


def triangle_area(base, height):
    area = base * height * 0.5  
    return area