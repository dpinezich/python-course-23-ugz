import math
def circle(radius):
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return area, circumference


f, u = circle(3)
print(f"Area: {round(f, 3)}, Circumference: {round(u, 3)}")