'''
Create a class Room with attributes room_number, room_type, price_per_night, is_booked.
Implement methods:

__str__ to return room details.
book_room() to mark a room as booked.
checkout_room() to mark it as available.
show_details() to display room information.
From Room, inherit:

DeluxeRoom with an extra attribute has_sea_view.
SuiteRoom with an extra attribute has_jacuzzi.
'''

class Room:
    def __init__(self, room_number, room_type, price_per_night, is_booked=False):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_booked = is_booked
    
    def __str__(self):
        status = "Booked" if self.is_booked else "Available"
        return f"Room {self.room_number}, Type: {self.room_type}, Price: ${self.price_per_night}/night, Status: {status}"
    
    def book_room(self):
        if not self.is_booked:
            self.is_booked = True
            print(f"Room {self.room_number} has been booked.")
        else:
            print(f"Room {self.room_number} is already booked.")
    
    def checkout_room(self):
        if self.is_booked:
            self.is_booked = False
            print(f"Room {self.room_number} is now available.")
        else:
            print(f"Room {self.room_number} is already available.")
    
    def show_details(self):
        print(self)

class DeluxeRoom(Room):
    def __init__(self, room_number, price_per_night, has_sea_view, is_booked=False):
        super().__init__(room_number, "Deluxe", price_per_night, is_booked)
        self.has_sea_view = has_sea_view
    
    def __str__(self):
        return super().__str__() + f", Sea View: {'Yes' if self.has_sea_view else 'No'}"
    
    def show_details(self):
        print(self)

class SuiteRoom(Room):
    def __init__(self, room_number, price_per_night, has_jacuzzi, is_booked=False):
        super().__init__(room_number, "Suite", price_per_night, is_booked)
        self.has_jacuzzi = has_jacuzzi
    
    def __str__(self):
        return super().__str__() + f", Jacuzzi: {'Yes' if self.has_jacuzzi else 'No'}"
    
    def show_details(self):
        print(self)

# Example usage
if __name__ == "__main__":
    deluxe = DeluxeRoom(101, 200, True)
    suite = SuiteRoom(202, 350, True)
    
    deluxe.show_details()
    suite.show_details()
    
    deluxe.book_room()
    deluxe.show_details()
    
    suite.book_room()
    suite.checkout_room()
    suite.show_details()


