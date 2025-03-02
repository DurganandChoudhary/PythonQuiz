'''
Create a class Movie with attributes title, director, duration, available_seats.
Implement methods:

__str__ to return movie details.
book_ticket() to reduce available seats.
cancel_ticket() to increase available seats.
show_details() to display movie information.
From Movie, inherit:

ActionMovie with an extra attribute stunt_level.
ComedyMovie with an extra attribute humor_rating.
'''

class Movie:
    def __init__(self, title, director, duration, available_seats):
        self.title = title
        self.director = director
        self.duration = duration
        self.available_seats = available_seats
    
    def __str__(self):
        return f"Movie: {self.title}, Director: {self.director}, Duration: {self.duration}, Available Seats: {self.available_seats}"
    
    def book_ticket(self):
        if self.available_seats > 0:
            self.available_seats -= 1
            print(f"Ticket booked for {self.title}. Remaining seats: {self.available_seats}")
        else:
            print(f"No available seats for {self.title}.")
    
    def cancel_ticket(self):
        self.available_seats += 1
        print(f"Ticket canceled for {self.title}. Available seats: {self.available_seats}")
    
    def show_details(self):
        print(self)

class ActionMovie(Movie):
    def __init__(self, title, director, duration, available_seats, stunt_level):
        super().__init__(title, director, duration, available_seats)
        self.stunt_level = stunt_level
    
    def __str__(self):
        return super().__str__() + f", Stunt Level: {self.stunt_level}"
    
    def show_details(self):
        print(self)

class ComedyMovie(Movie):
    def __init__(self, title, director, duration, available_seats, humor_rating):
        super().__init__(title, director, duration, available_seats)
        self.humor_rating = humor_rating
    
    def __str__(self):
        return super().__str__() + f", Humor Rating: {self.humor_rating}/10"
    
    def show_details(self):
        print(self)

# Example usage
if __name__ == "__main__":
    action_movie = ActionMovie("Mad Max: Fury Road", "George Miller", "120 mins", 100, "Extreme")
    comedy_movie = ComedyMovie("Superbad", "Greg Mottola", "113 mins", 80, 9)
    
    action_movie.show_details()
    comedy_movie.show_details()
    
    action_movie.book_ticket()
    action_movie.show_details()
    
    comedy_movie.cancel_ticket()
    comedy_movie.show_details()
