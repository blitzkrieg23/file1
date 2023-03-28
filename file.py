students = []
with open("students.csv") as file:
    for line in file:
        last,first= line.rstrip().split(",")
        students.append(f"{last} {first}")

for student in sorted(students):
    print(student)
