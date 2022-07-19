class Name:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
class Student:
    def __init__(self, studentName, enrolled):
        self.studentName = studentName
        self.GPA = 0.0
        self.creditHours = 0
        self.enrolled = enrolled
        self.classes = []



class Person:
    def __init__(self, name, eye_color, age):
        self.name = name
        self.age = age
        self.eye_color = eye_color


class Name:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


myPerson1= Person(Name('David', 'Joyner'), 'brown', 30)
myPerson2 = myPerson1