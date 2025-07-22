import random

options = ["rock", "paper", "scissors"]

def winner(player, computer):
    match (player, computer):
        case (p, c) if p == c:
            return " Well played! It's a tie!"
        case ("rock", "scissors") | ("scissors", "paper") | ("paper", "rock"):
            return " Congratulations! You win!"
        case ("rock", "paper") | ("scissors", "rock") | ("paper", "scissors"):
            return " Sorry! Computer wins!"

while True:
    player = input("\nRock, Paper, or Scissors?: ").lower()

    if player not in options:
        print("Invalid choice.")
        continue

    computer = random.choice(options)
    print(f"Computer chose: {computer}")
    print(winner(player, computer))

    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        break

