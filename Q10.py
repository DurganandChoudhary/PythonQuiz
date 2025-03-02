'''
Create a class Customer with attributes name, email, cart (list type).
Implement methods:

__str__ to return customer details.
add_to_cart(product_name) to add a product to the cart.
remove_from_cart(product_name) to remove a product.
show_details() to display customer information.
From Customer, inherit:

PremiumCustomer with an extra attribute discount_percentage.
GuestCustomer with an extra attribute valid_for_days.
'''


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = []
    
    def __str__(self):
        cart_items = ', '.join(self.cart) if self.cart else "Cart is empty"
        return f"Customer: {self.name}, Email: {self.email}, Cart: {cart_items}"
    
    def add_to_cart(self, product_name):
        self.cart.append(product_name)
        print(f"{product_name} added to cart.")
    
    def remove_from_cart(self, product_name):
        if product_name in self.cart:
            self.cart.remove(product_name)
            print(f"{product_name} removed from cart.")
        else:
            print(f"{product_name} not found in cart.")
    
    def show_details(self):
        print(self)

class PremiumCustomer(Customer):
    def __init__(self, name, email, discount_percentage):
        super().__init__(name, email)
        self.discount_percentage = discount_percentage
    
    def __str__(self):
        return super().__str__() + f", Discount: {self.discount_percentage}%"
    
    def show_details(self):
        print(self)

class GuestCustomer(Customer):
    def __init__(self, name, email, valid_for_days):
        super().__init__(name, email)
        self.valid_for_days = valid_for_days
    
    def __str__(self):
        return super().__str__() + f", Valid for: {self.valid_for_days} days"
    
    def show_details(self):
        print(self)

# Example usage
if __name__ == "__main__":
    premium = PremiumCustomer("Alice Johnson", "alice@example.com", 10)
    guest = GuestCustomer("Bob Smith", "bob@example.com", 7)
    
    premium.show_details()
    guest.show_details()
    
    premium.add_to_cart("Laptop")
    premium.add_to_cart("Smartphone")
    premium.show_details()
    
    guest.add_to_cart("Headphones")
    guest.remove_from_cart("Laptop")
    guest.show_details()









