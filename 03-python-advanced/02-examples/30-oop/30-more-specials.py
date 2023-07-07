class Vehicle:
    def __init__(self, br="(empty)", ac=0):
        self.brand = br
        self.acceleration = ac

    def __str__(self):
        return f"{self.brand} {self.acceleration} km/h"

    def __del__(self):
        print(f"Distance: {self}")
    def accelerate(self, value):
        self.acceleration += value

opel = Vehicle("Opel Admiral", 40)
renault = Vehicle("Renault Alpine")
fiat = Vehicle(ac=60)
mercedes = Vehicle()
print(opel)
print(renault)
print(fiat)
print(mercedes)
opel.accelerate(20)
print(opel.__dict__)
del opel
# print(opel)
