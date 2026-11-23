# Hailey Wilson
# 11/23/26
# Can they drive?
# Asks the user for their age and whether they have a permit, then prints whether they can drive or not.

age = int(input("Age: "))
permit = input("Have a permit? (y/n): ").lower()

if age >= 15 and permit == "y":
    print("You can drive with an adult.")
else:
    print("Not yet.")
