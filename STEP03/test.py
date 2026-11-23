total = 11.00

day = input("Day: ")
three_d = input("3D? (Y/N): ")
popcorn = input("Popcorn? (Y/N): ")

if day.lower() == "tuesday":
    total = total - 3.00
if three_d.upper() == "Y" or three_d.upper() == "YES":
    total = total + 2.50
if popcorn.lower() == "y" or popcorn.lower() == "yes":
    total = total + 5.50



print(f"Total: ${total:.2f}")
