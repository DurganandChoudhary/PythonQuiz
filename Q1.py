'''Create a class named Course that has instance variables title, instructor, price, lectures, users(list type), ratings,
 avg_rating. Implement the methods __str__, new_user_enrolled, received_a_rating and show_details. From the above class, inherit 
 two classes VideoCourse and PdfCourse. The class VideoCourse has instance variable length_video and PdfCourse has instance variable
 pages.'''


class Course:
    def __init__(self, title, instructor, price, lectures):
        self.title = title
        self.instructor = instructor
        self.price = price
        self.lectures = lectures
        self.users = []
        self.ratings = []
        self.avg_rating = 0

    def __str__(self):
        return f"Course: {self.title}, Instructor: {self.instructor}, Price: ${self.price}, Avg Rating: {self.avg_rating:.2f}"

    def new_user_enrolled(self, user):
        self.users.append(user)
        print(f"New user '{user}' enrolled in '{self.title}' course.")

    def received_a_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)
            self.avg_rating = sum(self.ratings) / len(self.ratings)
            print(f"Received a rating: {rating}. Updated average rating: {self.avg_rating:.2f}")
        else:
            print("Invalid rating! Please provide a rating between 1 and 5.")

    def show_details(self):
        print(f"Title: {self.title}")
        print(f"Instructor: {self.instructor}")
        print(f"Price: ${self.price}")
        print(f"Lectures: {self.lectures}")
        print(f"Users Enrolled: {len(self.users)}")
        print(f"Average Rating: {self.avg_rating:.2f}")

class VideoCourse(Course):
    def __init__(self, title, instructor, price, lectures, length_video):
        super().__init__(title, instructor, price, lectures)
        self.length_video = length_video

    def show_details(self):
        super().show_details()
        print(f"Total Video Length: {self.length_video} hours")

class PdfCourse(Course):
    def __init__(self, title, instructor, price, lectures, pages):
        super().__init__(title, instructor, price, lectures)
        self.pages = pages

    def show_details(self):
        super().show_details()
        print(f"Total Pages: {self.pages}")

# Example usage:
video_course = VideoCourse("Python Masterclass", "John Doe", 49.99, 30, 12)
pdf_course = PdfCourse("Data Science Guide", "Jane Smith", 29.99, 15, 200)

video_course.new_user_enrolled("Alice")
video_course.received_a_rating(5)
video_course.received_a_rating(4)
video_course.received_a_rating(6)  # Invalid rating test

print("\nVideo Course Details:")
video_course.show_details()

print("\nPDF Course Details:")
pdf_course.show_details()
