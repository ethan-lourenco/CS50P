# students.py

import csv

# # READ DATA
students = []

with open("students.csv") as file:
	reader = csv.DictReader(file)
	for row in reader:
		students.append({"name": row["name"], "home": row["home"]}) # or just .append(row)
		
# lambda is an anonymous function that is only used once and takes parameter student
for student in sorted(students, key=lambda student: student["name"]):
	print(f"{student['name']} is from {student['home']}")
	
# WRITE DATA
name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
	writer = csv.DictWriter(file, fieldnames=["name", "home"])
	writer.writerow({"name": name, "home": home})
