# Hailey Wilson
# 11/23/26
# Free shipping and gift wrap
# Calculates the total cost of an order

total = float(input("Order total: "))
wrap = input("Gift wrap? (y/n): ").lower()

if wrap == "y":
    total += 3

if total < 50:
    total += 5.99

print(f"Final total: ${total:.2f}")
