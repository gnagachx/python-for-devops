# define a class for fancy defining fancy cars

class FancyCar():
    # add class variable
    wheels = 4
    # add a method
    def driveFast(self):
        print("Driving so fast")

# Instantiate a fancy car
my_car = FancyCar()
# access class variable
my_car.wheels

# invoke method
my_car.driveFast()


'''
Fancycar --> class defines a method called driveFast and
an attribute wheels.

when you instantiate an instance of FancyCar named my_car, you can access the attribute and invoke the method using the dot syntax

'''

