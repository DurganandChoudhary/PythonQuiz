'''
Create a class Flight with attributes flight_number, destination, departure_time, available_seats.
Implement methods:

__str__ to return flight details.
book_seat() to decrease seat count.
cancel_seat() to increase seat count.
show_details() to display flight information.
From Flight, inherit:

DomesticFlight with an extra attribute airline_name.
InternationalFlight with an extra attribute passport_required (boolean).
'''

class Flight:
    def __init__(self, flight_number, destination, departure_time, available_seats):
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time
        self.available_seats = available_seats
    
    def __str__(self):
        return f"Flight {self.flight_number}, Destination: {self.destination}, Departure: {self.departure_time}, Seats Available: {self.available_seats}"
    
    def book_seat(self):
        if self.available_seats > 0:
            self.available_seats -= 1
            print(f"Seat booked on flight {self.flight_number}. Remaining seats: {self.available_seats}")
        else:
            print(f"No available seats on flight {self.flight_number}.")
    
    def cancel_seat(self):
        self.available_seats += 1
        print(f"Seat canceled on flight {self.flight_number}. Available seats: {self.available_seats}")
    
    def show_details(self):
        print(self)

class DomesticFlight(Flight):
    def __init__(self, flight_number, destination, departure_time, available_seats, airline_name):
        super().__init__(flight_number, destination, departure_time, available_seats)
        self.airline_name = airline_name
    
    def __str__(self):
        return super().__str__() + f", Airline: {self.airline_name}"
    
    def show_details(self):
        print(self)

class InternationalFlight(Flight):
    def __init__(self, flight_number, destination, departure_time, available_seats, passport_required):
        super().__init__(flight_number, destination, departure_time, available_seats)
        self.passport_required = passport_required
    
    def __str__(self):
        return super().__str__() + f", Passport Required: {'Yes' if self.passport_required else 'No'}"
    
    def show_details(self):
        print(self)

# Example usage
if __name__ == "__main__":
    domestic_flight = DomesticFlight("AI101", "New York", "10:00 AM", 100, "Air India")
    international_flight = InternationalFlight("BA205", "London", "8:00 PM", 50, True)
    
    domestic_flight.show_details()
    international_flight.show_details()
    
    domestic_flight.book_seat()
    domestic_flight.show_details()
    
    international_flight.cancel_seat()
    international_flight.show_details()
