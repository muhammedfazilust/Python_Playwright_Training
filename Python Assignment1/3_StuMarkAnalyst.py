students = {'Fz':45, 'Senna':48, 'Leclerc':18, 'Hamilton':35, 'Flora':9}

for name,marks in students.items():
    result = 'Pass' if marks > 20 else 'Fail'
    print(name +" : "+ result)