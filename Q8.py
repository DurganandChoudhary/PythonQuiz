'''
Create a class FoodItem with attributes name, price, cuisine, and availability.
Implement methods:

__str__ to return food item details.
update_availability(status) to mark an item as available/unavailable.
show_details() to display all details.
From FoodItem, inherit:

VegFood with an extra attribute vegan (boolean).
NonVegFood with an extra attribute meat_type

'''


class FoodItem:
    def __init__(self, name, price, cuisine, availability=True):
        self.name = name
        self.price = price
        self.cuisine = cuisine
        self.availability = availability
    
    def __str__(self):
        status = "Available" if self.availability else "Not Available"
        return f"Food: {self.name}, Price: ${self.price:.2f}, Cuisine: {self.cuisine}, Status: {status}"
    
    def update_availability(self, status):
        self.availability = status
        print(f"Availability of {self.name} updated to {'Available' if status else 'Not Available'}.")
    
    def show_details(self):
        print(self)

class VegFood(FoodItem):
    def __init__(self, name, price, cuisine, vegan, availability=True):
        super().__init__(name, price, cuisine, availability)
        self.vegan = vegan
    
    def __str__(self):
        return super().__str__() + f", Vegan: {'Yes' if self.vegan else 'No'}"
    
    def show_details(self):
        print(self)

class NonVegFood(FoodItem):
    def __init__(self, name, price, cuisine, meat_type, availability=True):
        super().__init__(name, price, cuisine, availability)
        self.meat_type = meat_type
    
    def __str__(self):
        return super().__str__() + f", Meat Type: {self.meat_type}"
    
    def show_details(self):
        print(self)

# Example usage
if __name__ == "__main__":
    veg_dish = VegFood("Paneer Tikka", 12.99, "Indian", True)
    non_veg_dish = NonVegFood("Chicken Biryani", 14.99, "Indian", "Chicken")
    
    veg_dish.show_details()
    non_veg_dish.show_details()
    
    veg_dish.update_availability(False)
    veg_dish.show_details()
    
    non_veg_dish.update_availability(True)
    non_veg_dish.show_details()


