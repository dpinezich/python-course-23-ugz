import random
random.seed

x = random.randint(-3, 3)

print("x:", x)

result = "positive" if x>0 else "negative"

print("This number is", result)
print("This number is", "positive" if x > 0 else "negative")

print("This number is",
"positive" if x > 0 else "negative" if x < 0 else "equals 0")