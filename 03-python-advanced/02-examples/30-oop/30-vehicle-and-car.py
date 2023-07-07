class Vehicle:
    def __init__(self, br, ac):
        self.brand = br
        self.acceleration = ac

    def accelerate(self, value):
        self.acceleration += value

    def __str__(self):
        return f"{self.brand} {self.acceleration} km/h"


class Car(Vehicle):
    def __init__(self, br, ac, pa):
        super().__init__(br, ac)
        self.passenger = pa

    def __str__(self):
        return f"{super().__str__()} {self.passenger} passengers"

    def board(self, num):
        self.passenger += num

    def exit(self, num):
        self.passenger -= num


fiat = Car("Fiat Marea", 50, 0)
fiat.board(3)
fiat.exit(1)
fiat.accelerate(10)
print(fiat)
