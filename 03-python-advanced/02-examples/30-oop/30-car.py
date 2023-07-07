class Car:
    velocity = 0

    def acceleration(self, value):
        self.velocity += value

    def output(self):
        print("Velocity:", self.velocity)
