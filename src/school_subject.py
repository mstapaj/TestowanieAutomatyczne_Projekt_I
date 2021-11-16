
class SchoolSubject:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def get_details(self):
        return {
            'name': self.name,
            'grades': self.grades
        }