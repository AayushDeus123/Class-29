#Inheritance (Child,Parent)
class Vehicle:
    def __init__ (self , name , maxspeed , mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage
        
class Bus(Vehicle):
    pass
bus = Bus('School Volvo' , 180 , 500)

print('The Name of the bus is',bus.name)
print('The MaxSpeed of the bus is',bus.maxspeed)
print('The Mileage of the bus is',bus.mileage)