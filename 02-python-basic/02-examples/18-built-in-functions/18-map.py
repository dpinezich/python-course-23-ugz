def quad(x):
    return x * x

def sum(a,b,c):
    return a + b + c


z = map(quad, [4, 2.5, -1.5])
print("Quadratic:")
for element in z:
    print(element)
print()

z = map(sum, [3, 1.2, 2], [4.8, 2], [5, 0.1, 9])
print("Sum:")
for element in z:
    print(element)