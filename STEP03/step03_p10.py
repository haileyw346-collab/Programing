# Hailey Wilson
# 11/23/26
# Member price
# Gives a price depending on whether the user is in the club or not and their grade

member = input("Club member? (y/n): ").lower()

if member == "y":
    grade = int(input("Grade: "))
    if grade == 12:
        price = 3
    else:
        price = 5
else:
    price = 8

print(f"Your price: ${price}")
