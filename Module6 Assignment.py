
class vehicle:
    def __init__(self,maxspeed,millage):
        self.maxspeed=maxspeed
        self.millage=millage
bmw=vehicle(200,10)
ferrari=vehicle(220,6)
print(bmw.maxspeed,bmw.millage)
print(ferrari.maxspeed,ferrari.millage)





class Vehicle:
    def __init__(self,name,max_speed,millage):
        self.name=name
        self.max_speed=max_speed
        self.millage=millage
class Bus(Vehicle):
    pass
volvo=Bus("White Schhol Volvo",180,12)
print(volvo.name,"Speed:",volvo.max_speed,"Millage:",volvo.millage)
class Car(Vehicle):
    pass
audi=Car("White Audi Q5",240,18)
print(audi.name,"Speed:",audi.max_speed,"Millage:",audi.millage)





class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
    def fare(self):
        return self.capacity * 100
class Bus(Vehicle):
    def fare1(self):
        amount = super().fare()
        amount =amount+ amount * 10 / 100
        return amount
School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare1()) 