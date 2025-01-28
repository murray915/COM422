
class cars:
    def __init__(self, make, model, year, color, maxSpeed, fuelLevel=100):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

        self.currentSpeed = 10
        self.maxSpeed = maxSpeed
        self.fuelLevel = fuelLevel

    def accelerate(self, amount):
        if self.fuelLevel > amount:
            self.currentSpeed += amount
            self.currentSpeed = min(self.currentSpeed, self.maxSpeed)
            self.fuelLevel -= amount
            self.fuelLevel = max(self.fuelLevel, 0)
        else:
            self.currentSpeed = 0

    def brake(self, amount):
        self.currentSpeed -= amount
        self.currentSpeed = max(self.currentSpeed, 0)

    def refuel(self, amount):
        self.fuelLevel += amount
        self.fuelLevel = min(self.fuelLevel, 100)
 
 
 