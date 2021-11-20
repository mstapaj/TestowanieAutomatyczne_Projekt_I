
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

    def edit_student(self, firstname=None, lastname=None, age=None):
        if isinstance(firstname, str):
            self.firstname = firstname
        elif firstname != None:
            raise Exception('Błedny typ danych w imieniu')
        if isinstance(lastname, str):
            self.lastname = lastname
        elif lastname != None:
            raise Exception('Błedny typ danych w nazwisku')
        if isinstance(age, int) and str(age) != 'True' and str(age) != 'False' and 0 < age:
            self.age = age
        elif age != None:
            raise Exception('Błedny typ danych w wieku')
        return {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'age': self.age
        }