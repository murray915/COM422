from car import cars

car1 = cars("BMW", "Series 3", 2022, "White", 180)
car2 = cars("Audi", "A4", 2021, "Black", 200)

car1.accelerate(100)
car1.accelerate(2)
car1.brake(0)
car1.refuel(0)
car2.accelerate(1)
car2.refuel(2)
car2.brake(4)

print(f"\nMake: {car1.make}, Model: {car1.model}, Current Speed: {car1.currentSpeed}, Fuel Level: {car1.fuelLevel}")
print(f"\nMake: {car2.make}, Model: {car2.model}, Current Speed: {car2.currentSpeed}, Fuel Level: {car2.fuelLevel}")