# Simple Employee File Management
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR,"employees.txt")

class Employee:
    def __init__(self,employee_id, name, role, salary):
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.salary = salary

    def display_details(self):
        print(f"{self.employee_id} - {self.name} - {self.role} - {self.salary}")

    def to_line(self):
        #convert employee to a line for the txt file
        return f"{self.employee_id},{self.name},{self.role},{self.salary}"

    @classmethod
    def from_line(cls, line):
        #create an employee object from a line of txt file
        employee_id, name, role, salary = line.strip().split(",")
        return cls(int(employee_id),name.strip(),role.strip(),int(salary))

def add_employee(employee):
    with open(FILE_NAME,"a") as file:
        file.write(employee.to_line()+"\n")

def read_employee():
    employees = []
    try:
        with open(FILE_NAME,"r") as file:
            for line in file:
                if line.strip():
                    employees.append(Employee.from_line(line))
    except FileNotFoundError:
        print(f"Error: '{FILE_NAME}' was not found. Please create the file first")
    except ValueError:
        print(f"Error: '{FILE_NAME}' contains invalid formatted record")
    return employees


def find_highest_earners(employees):
    return [i for i in employees if i.salary> 50000]

def find_highest_salary(employees):
    if not employees:
        return None
    return max(employees, key= lambda i : i.salary)

def find_employee_by_role(employees):
    by_role = {}
    for employee in employees:
        by_role.setdefault(employee.role, []).append(employee)
    return by_role

def main():
    employees = read_employee()
    if not employees:
        print("No employee data to display")
        return

    print(" Employee Details ")

    for employee in employees:
        employee.display_details()

    print("\n Employee with Salary > 50000 ")
    for employee in find_highest_earners(employees):
        print(f"{employee.name} - {employee.salary}")

    highest = find_highest_salary(employees)
    print(f"Highest paid employee: {highest.name} - {highest.salary}")

    print("\n Employee Count by Role ")
    by_role = find_employee_by_role(employees)
    for role in by_role:
        print(f"{role}: {len(by_role[role])}")


if __name__ == "__main__":
    main()