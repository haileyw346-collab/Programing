# Hailey Wilson
# 11/23/26
# Gym Day Pass
#


#Named constants
CHILD_PRICE = 4.00
STUDENT_PRICE = 6.00
ADULT_PRICE = 9.00
WEEKEND_CHARGE = 2.00
TOWEL_PRICE = 1.50

# input
name = input("Name: ")
age = int(input("Age: "))
day = input("Day of the week: ").lower()
towel = input("Rent a towel? (y/n): ").lower()

#check if age is within range
if age < 5 or age > 100:
    print("Error: age must be 5 to 100")
else:
    total = 0.0
    #determine pass type
    if age < 13:
        pass_type = "Child"
        base_price = CHILD_PRICE
    elif age <= 18:
        pass_type = "Student"
        base_price = STUDENT_PRICE
    else:
        pass_type = "Adult"
        base_price = ADULT_PRICE

    print(f"\n--- Day Pass for {name} ---")
    print(f"Pass type:  {pass_type}")
    print(f"Base price: ${base_price:.2f}")

    #calculations
    total = base_price
    
    if day == "saturday" or day == "sunday":
        print(f"Weekend:    ${WEEKEND_CHARGE:.2f}")
        total = total + WEEKEND_CHARGE
        
    if towel == "y":
        print(f"Towel:      ${TOWEL_PRICE:.2f}")
        total = total + TOWEL_PRICE
    print(f"Total:      ${total:.2f}")
