class Person:
    def __init__(self, name, weight, hunger, energy):
        if(hunger < 0 or hunger > 100):
            raise Exception("Hunger must be between 0 and 100")
        elif (energy < 0 or energy > 100):
            raise Exception("Energy must be between 0 and 100")
 
        self.name = name
        self.weight = weight
        self.hunger = hunger
        self.energy = energy
 
    def rest(self):
        self.energy = self.energy+1
        self.hunger = self.hunger+1
 
    def run(self, miles):
        # For every mile, the person will lose/gain two units
        change = miles * 2
        print(change)

        if self.energy-change > 0 and self.hunger+change <= 100:
            self.energy = self.energy-change
            self.hunger = self.hunger+change
            return True
        return False
    
    def print(self):        
        print(self.energy)



p1 = Person("abc", 150, 100, 10)
p1.print()

p1.run(2)
p1.print()