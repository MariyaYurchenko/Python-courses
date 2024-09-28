import csv

fileName = "csv/students2.csv"
name = input("What's your name? ")
home = input("Where is your home? ")

with open(fileName, "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})

students = []

try: 
    with open(fileName) as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)  
except FileNotFoundError:
        print("No such file", fileName)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} lives in {student['home']}")