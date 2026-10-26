class Student:
    def __init__(self,name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
            print(f"Name:{self.name}, RollNo:{self.roll_number}, Marks{self.marks}")

    def check_result(self):
            return 'Pass' if self.marks >= 40 else 'Fail'

stu1 = Student('Xavier',101,45)
stu2 = Student('Quiton',102,35)
stu3 = Student('Neela',103,55)

students = [stu1, stu2, stu3]
for student in students:
    student.display_details()
    print(f"Result: {student.check_result()}\n")