# Hailey Wilson
# 11/23/26
# Check the range first
# Asks for a rating and checks if it is in range before printing

rating = int(input("Rating (1-5): "))

if rating < 1 or rating > 5:
    print("Error: rating must be 1 to 5")
else:
    print(f"Thanks for the rating of {rating}!")
