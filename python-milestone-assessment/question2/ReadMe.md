# Question 2 - Simple Employee File Management

## Problem Statement
Maintain employee records in a text file and read them to generate a simple report. The report should show all employees, 
those earning more than ₹50,000, the highest-paid employee, and the employee count per role.

## Approach / Logic
1. Employee data is stored in `employees.txt`, one record per line, in the format `ID,Name,Role,Salary`.
2. `read_employees()` opens the file using a context manager (`with open()`), parses each line, and creates an `Employee`
   object. If the file is missing, a `FileNotFoundError` is caught and handled.
4. `Employee` is a class with `employee_id`, `name`, `role`, `salary`, a `display_details()` method, and
    helper methods for converting to and from file lines.
6. `find_high_earners()` uses a list comprehension to filter salaries above ₹50,000.
7. `find_highest_salary()` uses `max()` with a lambda on salary.
8. `find_employees_by_role()` groups employees into a dictionary keyed by role. Counts are taken with `len()`.
9. `add_employee()` appends a new record to the file in append mode.

## How to Run
```bash
cd question2
python main.py
```
Keep `employees.txt` in the same folder as `main.py`. Requires Python 3.6 or higher.

## Sample Input (employees.txt)

101,Rahul,Python Developer,50000
102,Anjali,Tester,45000
103,John,Developer,60000
104,Priya,Tester,48000

## Sample Output

===== Employee Details =====
101 - Rahul - Python Developer - ₹50000
102 - Anjali - Tester - ₹45000
103 - John - Developer - ₹60000
104 - Priya - Tester - ₹48000

===== Employees with Salary > 50000 =====
John - ₹60000

Highest Paid Employee: John - ₹60000

Employee Count by Role:
Developer: 1
Python Developer: 1
Tester: 2


## Python Concepts Used
- File handling (reading and appending with `open()`)
- Context manager (`with` statement)
- Exception handling (`try / except FileNotFoundError` and `ValueError`)
- Classes and objects (`Employee` class)
- Constructor (`__init__`) and methods (`display_details`, `to_line`)
- `@classmethod` for creating objects from file lines
- Functions (`add_employee`, `read_employees`, `find_highest_salary`, `find_employees_by_role`, `find_high_earners`)
- Lists and dictionaries (storing employees and grouping by role)
- List comprehension and `max()` with a lambda
- String manipulation (`split`, `strip`)
