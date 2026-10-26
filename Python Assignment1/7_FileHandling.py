def cmpltFile():
    with open('notes.txt','r') as file:
        content = file.read()
        return "Complete File\n"+ content + '\n'

with open('notes.txt','w') as file:
    file.write("Hello\n")
    file.write("How\n")
    file.write("are\n")
    file.write("you\n")
    file.write("Steve!\n")

print(cmpltFile())

with open('notes.txt','r') as file:
    line = file.readlines()
    print("Third line : " + line[2] + '\n')

with open('notes.txt','a') as file:
    file.write("\nNew line added")

print(cmpltFile())