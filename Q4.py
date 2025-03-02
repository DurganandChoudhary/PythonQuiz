'''
Create a base class Vehicle with attributes brand, model, year, rental_price, is_available.
Implement methods:

__str__ to return vehicle details.
rent_vehicle() to mark the vehicle as unavailable.
return_vehicle() to mark the vehicle as available.
show_details() to display all details.
From Vehicle, inherit:

Car with an extra attribute num_seats.
Bike with an extra attribute engine_capacity.

'''

class Vehicle:
    def __init__(self, brand, model, year, rental_price, is_available=True):
        self.brand = brand
        self.model = model
        self.year = year
        self.rental_price = rental_price
        self.is_available = is_available
    
    def __str__(self):
        availability = "Available" if self.is_available else "Not Available"
        return f"{self.year} {self.brand} {self.model}, Rental Price: ${self.rental_price}/day, Status: {availability}"
    
    def rent_vehicle(self):
        if self.is_available:
            self.is_available = False
            print("Vehicle rented successfully.")
        else:
            print("Sorry, this vehicle is not available.")
    
    def return_vehicle(self):
        self.is_available = True
        print("Vehicle returned successfully.")
    
    def show_details(self):
        print(self)

class Car(Vehicle):
    def __init__(self, brand, model, year, rental_price, num_seats, is_available=True):
        super().__init__(brand, model, year, rental_price, is_available)
        self.num_seats = num_seats
    
    def __str__(self):
        return super().__str__() + f", Seats: {self.num_seats}"
    
    def show_details(self):
        print(self)

class Bike(Vehicle):
    def __init__(self, brand, model, year, rental_price, engine_capacity, is_available=True):
        super().__init__(brand, model, year, rental_price, is_available)
        self.engine_capacity = engine_capacity
    
    def __str__(self):
        return super().__str__() + f", Engine Capacity: {self.engine_capacity}cc"
    
    def show_details(self):
        print(self)

# Example usage
if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2022, 50, 5)
    bike = Bike("Yamaha", "R15", 2021, 30, 155)
    
    car.show_details()
    bike.show_details()
    
    car.rent_vehicle()
    car.show_details()
    
    car.return_vehicle()
    car.show_details()


