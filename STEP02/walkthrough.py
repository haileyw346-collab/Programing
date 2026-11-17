# Name: Hailey Wilson
# Date: 2026-11-12
# Program: Carpet Cost Example
# Description: Calculate cost to carpet room

#Named constant for install fee
INSTALL_FEE = 25.00

# Input: room owner, cost per square foot, and
owner = input("Owner: ")
cost_per_foot = float(input("Cost per square foot: "))
square_feet = int(input("Square feet: "))

# Processing: Material cost and total
material_cost = cost_per_foot * square_feet
total_cost = INSTALL_FEE + material_cost

#Output: a small report, format $ to 2 decimal places
print(f"--- Estimate for {owner} ---")
print(f"Material: ${material_cost:.2f}")
print(f"Install:  ${INSTALL_FEE:.2f}")
print(f"Total:    ${total_cost:.2f}")
