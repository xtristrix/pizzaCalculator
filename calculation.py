import math


def radius(a):
    b = a / 2
    return b

def area(a):
    pizzaArea = ((a/2) ** 2) * math.pi
    return pizzaArea

def pricePerSquareCM(price, area):
    pricePerSquareCM = price / area
    return pricePerSquareCM