# Hailey Wilson
# 11/23/26
# Late fee
# calculates the late fee for a library book

FEE_PER_DAY = 0.25
MAX_FEE = 5.00

days_late = int(input("Days late: "))

fee = FEE_PER_DAY * days_late

if fee > MAX_FEE:
    fee = MAX_FEE

print(f"Late fee: ${fee:.2f}")
