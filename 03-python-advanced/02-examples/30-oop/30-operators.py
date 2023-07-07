class Vehicle:
    def __init__(self, br, ac):
        self.brand = br
        self.acceleration = ac

    def __gt__(self, other):
        return self.acceleration > other.acceleration

    def __eq__(self, other):
        return self.acceleration == other.acceleration

    def __sub__(self, other):
        return self.acceleration - other.acceleration



opel = Car("Opel Admiral", 60)
volvo = Car("Volvo Amazon", 45)
if opel > volvo:
    print("Opel is faster")
elif opel == volvo:
    print("Both are the same")
else:
    print("Volvo is faster")

diff = opel - volvo
print(f"Difference of Speed: {diff} km/h")