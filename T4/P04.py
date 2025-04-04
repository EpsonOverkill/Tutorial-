class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    def dataprint(self):
        print(f"Name: {self.name}, Roll No: {self.roll}")
stud1 = Student("Gouri", 40)
stud2 = Student("Nidhi", 48)
stud1.dataprint()
stud2.dataprint()
