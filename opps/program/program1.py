class Car:
    
    def __init__(self, make, model, year):
        self.make = make        
        self.model = model
        self.year = year

    def description(self):     
        return f"{self.year} {self.make} {self.model}"


car1 = Car("Honda", "Civic", 2020)
car2 = Car("Toyota", "Corolla", 2022)

print(car1.description())  
print(car2.description())  
