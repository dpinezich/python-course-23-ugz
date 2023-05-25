def sumfunc(*params):
    result = 0
    for s in params:
        result += s
    return result

print("Sum:", sumfunc(3, 4))
print("Sum:", sumfunc(3, 8, 12, -5))