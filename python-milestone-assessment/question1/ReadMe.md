# Question 1 - Student Marks Management System

## Problem Statement
Develop a Python program that accepts details of multiple students (ID, name, and marks in Python, SQL and AI), calculates the total, 
average and grade for each student, shows PASS/FAIL status, and identifies the highest scorer and students with an average above 75.

## Approach / Logic
1. Ask the user how many students to enter, then collect each student's ID, name and marks. Marks are validated to be between 0 and 100.
2. Store each student as a dictionary and keep all students in a list.
3. For each student:
   - Total = Python + SQL + AI
   - Average = Total / 3
   - Grade is decided by `get_grade()` (A ≥ 80, B ≥ 60, C ≥ 50, D ≥ 40, F < 40)
   - Result is PASS if average ≥ 40, otherwise FAIL
4. Use `max()` with a lambda to find the highest average.
5. Use a list comprehension to collect names of students with average > 75.

## How to Run
```bash
cd question1
python main.py
```
Requires Python 3.6 or higher. No external libraries are needed.

## Sample Input
4
101
Rahul
85
78
77
102
Deva
60
70
65
103
Jiya
80
78
76
104
Sana
35
40
38

## Sample Output

===== Student Result =====
Student ID: 101
Name: Rahul
Total: 240
Average: 80.00
Grade: A
Result: PASS

Student ID: 102
Name: Deva
Total: 195
Average: 65.00
Grade: B
Result: PASS

Student ID: 103
Name: Jiya
Total: 234
Average: 78.00
Grade: A
Result: PASS

Student ID: 104
Name: Sana
Total: 113
Average: 37.67
Grade: F
Result: FAIL

Highest Scoring Student: Rahul (Average: 80.00)
Students above 75: Rahul, Jiya


## Python Concepts Used
- Lists and dictionaries (storing students and results)
- Functions (`get_grade`, `input_marks`, `input_students`, `calculate_results`, `display_results`, `find_highest_average`)
- Conditional statements (`if / elif / else` for grades and PASS/FAIL)
- Loops (`for` loops over students and subjects, `while` loop for validation)
- List comprehension (names of students above 75)
- `max()` with a lambda function
- Exception handling (`try / except Exception`) for input validation
- String formatting (f-strings with format{`.2f`})
