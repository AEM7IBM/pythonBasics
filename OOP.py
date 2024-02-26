class course:
    def __init__(self, name):
        self.name = name
        self.students = []
    def add_students(self, student):
        self.students.append(student)