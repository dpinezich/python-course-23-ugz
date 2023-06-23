a: int = 42
b: float = 42.5
c: str = "Hallo"
d: bool = True

print("Variables:", a, b, c, d)


def average(x: float, y: float) -> float:
    result = (x + y) / 2
    return result


print("Average:", average(3.4, 9.4))