def sum(a, b):
    c = a + b


result = sum(7, 12)
if not result:
    print("Error")
if result is None:
    print("Error")

print("Result:", result)
print("Boolean Value", bool(result))
print("Type:", type(result))
