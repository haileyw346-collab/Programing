# Hailey Wilson
# 11/24/26
# Password checker
# 

PASSWORD = "python123"
guess = input("Enter the password: ")

while guess != PASSWORD:
    print("Try again!")
    guess = input("Enter the password: ")

print("Access granted!")