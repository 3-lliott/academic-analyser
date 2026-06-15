students = []

num_students = int(input("How many students? "))

for i in range(num_students):
    name = input(f"Enter name for student {i + 1}: ")
    score = float(input(f"Enter score for {name}: "))
    students.append({"name": name, "score": score})

print("\n--- Grade Report ---")

total = 0

for student in students:
    score = student["score"]
    total += score

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"{student['name']}: {score} - {grade}")

average = total / len(students)
print(f"\nClass Average: {average:.1f}")