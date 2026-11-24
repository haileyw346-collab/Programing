answer = "yes"
rounds = 0

while answer == "yes":
    rounds = rounds + 1
    print(f"Playing round {rounds}...")
    answer = input("Play again? (yes/no): ").lower()

print(f"Thanks for playing {rounds} rounds.")