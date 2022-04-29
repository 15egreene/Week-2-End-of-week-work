from cmath import pi
import math 



def square_feet(length, width):
    area = length * width
    return area
    # print(area)

print(square_feet(100,200))


def circumference(x):
    radius = float(input("what is your radius? "))
    circumference = 2 * pi * radius
    radius = input("what is your radius? ")
    empty_string = circumference
    return empty_string
circumference(12)
