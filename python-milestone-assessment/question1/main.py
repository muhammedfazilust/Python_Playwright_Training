# Student Marks Management System
SUBJECTS = ["Python","SQL","AI"]

def get_grade(average):
    if average>=80:
        return 'A'
    elif average>=60:
        return 'B'
    elif average>=50:
        return 'C'
    elif average>=40:
        return 'D'
    return 'F'

def input_marks(subject):
    while True:
        try:
            marks = int(input(f"{subject} marks (0-100): "))
            if 0<=marks and marks<=100:
                return marks
            print("Marks must be between 0 and 100")
        except Exception:
            print("Please enter a whole number")

def input_students():
    students = []
    count = int(input("Enter number of students : "))

    for i in range(1, count+1):
        print(f"\nStudent {i}")
        student_id = input("Student ID : ")
        name = input("Name : ")

        student = {"id": student_id, "name": name}
        for subject in SUBJECTS:
            student[subject.lower()] = input_marks(subject)
        students.append(student)

    return students

def calculate_results(students):
    print(students)
    results = []
    for student in students:
        total = student["python"] + student["sql"] + student["ai"]
        average = total/len(SUBJECTS)

        results.append({
            "id" : student["id"],
            "name" : student["name"],
            "total" : total,
            "average" : round(average,2),
            "grade" : get_grade(average),
            "result" : "PASS" if average>=40 else "FAIL"
        })

        return results

def display_results(results):
    print("\n Students Results ")
    for i in results:
        print(f"Student Id : {i['id']}")
        print(f"Name : {i['name']}")
        print(f"Total : {i['total']}")
        print(f"Average : {i['average']}")
        print(f"Grade: {i['grade']}")
        print(f"Result: {i['result']}\n")

def find_highest_average(results):
    return max(results, key=lambda i:i["average"])

def main():
    students = input_students()
    results = calculate_results(students)
    display_results(results)

    top = find_highest_average(results)
    print(f"Highest scoring student: {top['name']} (Average: {format(top['average'],'.2f')})")

    above_75 = [i["name"] for i in results if i["average"]>75]
    print("Students above 75: "+ (", ".join(above_75) if above_75 else "None"))


if __name__ == "__main__":
    main()