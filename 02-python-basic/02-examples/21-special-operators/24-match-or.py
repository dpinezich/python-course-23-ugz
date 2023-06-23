import random
x = random.randint(1,6)
print("x =", x)

match x:
    case 1 | 3 | 5:
        print("uneven")
    case 2 | 4 | 6:
        print("even")
    case _:
        print("no value")
