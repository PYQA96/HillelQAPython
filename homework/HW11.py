class Car:

    def __init__(self,wheels=4,mode_of_transports="Private"):
        self.wheels=wheels
        self.mode_of_transports=mode_of_transports

    @property
    def wheel(self):
        return self.wheels


    @property
    def mode_of_transport(self):
        return self.mode_of_transports


    def __repr__(self):
        return str(self.__dict__)


class Bus(Car):

    def __init__(self,Company="TOW Awto"):
        Car.__init__(self,wheels=4,mode_of_transports="Public")
        self.Company=Company




Ikarus=Bus()
Tesla=Car()
list_of_car=[Ikarus,Tesla]
for objects in list_of_car:
    print(objects.wheels,objects.mode_of_transports,objects)


class Vehicle(Car):


    def __init__(self,name):
        Car.__init__(self,mode_of_transports="Neopredelen")
        self.name=name


    def desc(self):
        return self.name


Nisssan = Vehicle("Lastohka")
print(Nisssan)


class Vehicle:
    def desc(self):
        print("This is a generic vehicle.")

    def wheels(self):
        print("It has an unspecified number of wheels.")


class Car(Vehicle):
    def desc(self):
        print("This is a car.")

    def wheels(self):
        print("It has 4 wheels.")


class Bike(Vehicle):
    def desc(self):
        print("This is a bike.")

    def wheels(self):
        print("It has 2 wheels.")