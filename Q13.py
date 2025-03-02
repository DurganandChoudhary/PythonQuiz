'''
Create a class Course with attributes course_name, instructor, duration, max_students.
Implement methods:

__str__ to return course details.
enroll_student(student_name) to enroll a student if seats are available.
drop_student(student_name) to remove a student.
show_details() to display all details.
From Course, inherit:

OnlineCourse with an extra attribute platform.
OfflineCourse with an extra attribute classroom_number.
'''

class Course:
    def __init__(self, course_name, instructor, duration, max_students):
        self.course_name = course_name
        self.instructor = instructor
        self.duration = duration
        self.max_students = max_students
        self.enrolled_students = []
    
    def __str__(self):
        return f"Course: {self.course_name}, Instructor: {self.instructor}, Duration: {self.duration}, Max Students: {self.max_students}, Enrolled: {len(self.enrolled_students)}"
    
    def enroll_student(self, student_name):
        if len(self.enrolled_students) < self.max_students:
            self.enrolled_students.append(student_name)
            print(f"{student_name} has been enrolled in {self.course_name}.")
        else:
            print(f"Course {self.course_name} is full. Enrollment failed.")
    
    def drop_student(self, student_name):
        if student_name in self.enrolled_students:
            self.enrolled_students.remove(student_name)
            print(f"{student_name} has been dropped from {self.course_name}.")
        else:
            print(f"{student_name} is not enrolled in {self.course_name}.")
    
    def show_details(self):
        print(self)

class OnlineCourse(Course):
    def __init__(self, course_name, instructor, duration, max_students, platform):
        super().__init__(course_name, instructor, duration, max_students)
        self.platform = platform
    
    def __str__(self):
        return super().__str__() + f", Platform: {self.platform}"
    
    def show_details(self):
        print(self)

class OfflineCourse(Course):
    def __init__(self, course_name, instructor, duration, max_students, classroom_number):
        super().__init__(course_name, instructor, duration, max_students)
        self.classroom_number = classroom_number
    
    def __str__(self):
        return super().__str__() + f", Classroom: {self.classroom_number}"
    
    def show_details(self):
        print(self)

# Example usage
if __name__ == "__main__":
    online_course = OnlineCourse("Python Programming", "Dr. Smith", "10 weeks", 50, "Udemy")
    offline_course = OfflineCourse("Data Science", "Prof. Johnson", "12 weeks", 30, "Room 101")
    
    online_course.show_details()
    offline_course.show_details()
    
    online_course.enroll_student("Alice")
    online_course.show_details()
    
    offline_course.enroll_student("Bob")
    offline_course.drop_student("Alice")
    offline_course.show_details()


