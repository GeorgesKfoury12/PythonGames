import random

def play():
    user = input("Chose on of the following 'r' for rock, 'p' for paper, 's' for scissors: ").lower()
    computer = random.choice(["r", "p", "s"])
    print(f"You chose '{user}' and computer chose '{computer}'.")
    if user == computer:
        return "Tie"
    if is_win(user, computer):
        return "You Win!"
    return "You Lose!"

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())