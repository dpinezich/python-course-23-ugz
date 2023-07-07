class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def accelerate(self, value):
        self.speed += value

    def printout(self):
        print("Speed:", self.speed)


volvo = Vehicle(0)
opel = Vehicle(0)
volvo.printout()
volvo.accelerate(20)
volvo.printout()
opel.printout()