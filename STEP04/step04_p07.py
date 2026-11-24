# Hailey Wilson
# 11/24/26
# Add numbers until zero
# keeps asking for numbers and adding them until 0 is given, then prints the total.

total = 0

num = int(input("Enter a umber (0 to stop): "))

while num != 0:
    total = total + num
    num = int(input("Enter a umber (0 to stop): "))

print(f"The total is {total}")