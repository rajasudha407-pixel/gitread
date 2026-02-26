name = input("Enter student name: ")
mark1 = float(input("Enter marks for Subject 1 (0-100): "))
mark2 = float(input("Enter marks for Subject 2 (0-100): "))
mark3 = float(input("Enter marks for Subject 3 (0-100): "))
total_marks = mark1 + mark2 + mark3
percentage = (total_marks / 300) * 100
if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"
print("\nOutput:")
print(f"{name}")
print(f"Total: {int(total_marks)}/300")
print(f"Percentage: {percentage:.1f}%")
print(f"Grade: {grade}")

