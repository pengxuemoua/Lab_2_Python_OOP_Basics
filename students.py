class Student:
    def __init__(self, name, school_id, gpa):
        self.name = name
        self.school_id = school_id
        self.gpa = gpa

    def __str__(self):
        return f"Student Name: {self.name}, School ID: {self.school_id}, GPA: {self.gpa}"


