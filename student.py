import csv

students = []

fileName = "students.csv"
try:
    with open(fileName) as file:
        reader = csv.reader(file)
except FileNotFoundError:
    print("No such file:", fileName)
else:
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} lives in {student['home']}")
