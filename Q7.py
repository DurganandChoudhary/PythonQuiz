'''
Create a class Student with attributes name, student_id, grade, subjects (list type).
Implement methods:

__str__ to return student details.
enroll(subject) to add a subject to the list.
drop_subject(subject) to remove a subject from the list.
show_details() to display all student information.
From Student, inherit:

Undergraduate with an extra attribute major.
Postgraduate with an extra attribute thesis_topic

'''

class Student:
    def __init__(self, name, student_id, grade, subjects=None):
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.subjects = subjects if subjects else []
    
    def __str__(self):
        subjects_list = ', '.join(self.subjects) if self.subjects else "No subjects enrolled"
        return f"Student ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}, Subjects: {subjects_list}"
    
    def enroll(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)
            print(f"Enrolled in {subject}.")
        else:
            print(f"Already enrolled in {subject}.")
    
    def drop_subject(self, subject):
        if subject in self.subjects:
            self.subjects.remove(subject)
            print(f"Dropped {subject}.")
        else:
            print(f"Not enrolled in {subject}.")
    
    def show_details(self):
        print(self)

class Undergraduate(Student):
    def __init__(self, name, student_id, grade, major, subjects=None):
        super().__init__(name, student_id, grade, subjects)
        self.major = major
    
    def __str__(self):
        return super().__str__() + f", Major: {self.major}"
    
    def show_details(self):
        print(self)

class Postgraduate(Student):
    def __init__(self, name, student_id, grade, thesis_topic, subjects=None):
        super().__init__(name, student_id, grade, subjects)
        self.thesis_topic = thesis_topic
    
    def __str__(self):
        return super().__str__() + f", Thesis Topic: {self.thesis_topic}"
    
    def show_details(self):
        print(self)

# Example usage
if __name__ == "__main__":
    undergrad = Undergraduate("Alice Johnson", "UG123", "A", "Computer Science", ["Math", "Physics"])
    postgrad = Postgraduate("Bob Smith", "PG456", "A+", "AI in Healthcare", ["Machine Learning", "Data Science"])
    
    undergrad.show_details()
    postgrad.show_details()
    
    undergrad.enroll("Chemistry")
    undergrad.drop_subject("Math")
    undergrad.show_details()
    
    postgrad.enroll("Deep Learning")
    postgrad.show_details()







