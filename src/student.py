
class Student:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.subjects = []

    def get_details(self):
        return {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'age': self.age
        }