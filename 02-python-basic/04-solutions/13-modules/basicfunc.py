def average_of_4(a, b, c, d):
    return (a + b + c + d) / 4


def compare(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0


def fahrenheit2celsius(temp_fahrenheit):
    return (temp_fahrenheit - 32) * 5 / 9
