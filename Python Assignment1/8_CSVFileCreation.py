import csv

data = [['id','name','salary'],
        [1,'Fz',10000],
        [2,'Steve Harrington', 17500],
        [3,'Davis',12000],
        [4,'Yuki',6500]]

with open('employee.csv','w',newline='') as file:
    write = csv.writer(file)
    write.writerows(data)
    print(write)

with open('employee.csv','a',newline='') as file:
    write = csv.writer(file)
    write.writerow([5,'Salah',30000])
    print(write)