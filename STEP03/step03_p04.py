# Hailey Wilson
# 11/23/26
# Letter grade
# Asks for a score and prints the corresponding letter grade.

score = int(input("Score: "))
grade = ""
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

print(f"Grade: {grade}")
