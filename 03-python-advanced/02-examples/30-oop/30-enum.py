import enum


class Color(enum.IntEnum):
    red = 5
    yellow = 2
    blue = 4


x = 2
if x == Color.yellow:
    print("This is yellow")

print(Color.yellow)
print(Color.yellow * 10)
