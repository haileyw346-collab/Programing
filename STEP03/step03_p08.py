# Hailey Wilson
# 11/23/26
# Bigger number
# Asks for two numbers and prints witch one os bigger, or if they are equal

numA = int(input("First number: "))
numB = int(input("Second number: "))

if numA > numB:
    print(f"{numA} is bigger.")
elif numA < numB:
    print(f"{numB} is bigger.")
else:
    print("They are equal.")
