# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand = brand 

    def start(self):      
        return "Engine started!"

my_car = Car("Toyota")

print(my_car.brand)    
print(my_car.start()) 