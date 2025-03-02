'''
Create a class Person with attributes name, age, gender.
Implement methods:

__str__ to return person details.
show_details() to display all information.
From Person, inherit:

Doctor with extra attributes specialization and years_of_experience.
Patient with extra attributes disease and admitted_date.
'''

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
    
    def show_details(self):
        print(self)

class Doctor(Person):
    def __init__(self, name, age, gender, specialization, years_of_experience):
        super().__init__(name, age, gender)
        self.specialization = specialization
        self.years_of_experience = years_of_experience
    
    def __str__(self):
        return super().__str__() + f", Specialization: {self.specialization}, Experience: {self.years_of_experience} years"
    
    def show_details(self):
        print(self)

class Patient(Person):
    def __init__(self, name, age, gender, disease, admitted_date):
        super().__init__(name, age, gender)
        self.disease = disease
        self.admitted_date = admitted_date
    
    def __str__(self):
        return super().__str__() + f", Disease: {self.disease}, Admitted Date: {self.admitted_date}"
    
    def show_details(self):
        print(self)

# Example usage
if __name__ == "__main__":
    doctor = Doctor("Dr. Alice Johnson", 45, "Female", "Cardiology", 20)
    patient = Patient("Bob Smith", 60, "Male", "Pneumonia", "2024-02-15")
    
    doctor.show_details()
    patient.show_details()








