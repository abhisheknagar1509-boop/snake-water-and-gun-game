# Import random module
import random
print('Snake - Water - Gun')

# Input no. of rounds
n = int(input('Enter number of rounds: '))

# List containing Snake(s), Water(w), Gun(g)
options = ['s', 'w', 'g']

# Round numbers
rounds = 1

# Count of computer wins
comp_win = 0

# Count of player wins
user_win = 0

# There will be n rounds of game
while rounds <= n:

    # Display round
    print(f"\nRound : {rounds}\nSnake - 's'\nWater - 'w'\nGun - 'g'")

    # Exception handling
    try:
        player = input("Choose your option: ").lower()
    except EOFError as e:
        print(e)

    # Control of bad inputs
    if player not in options:
        print("Invalid input, try again\n")
        continue

    # Computer’s turn
    computer = random.choice(options)
    print(f"Computer chose: {computer}")

    # Conditions based on the game rule
    if computer == player:
        print("Draw!!\n")
    elif (computer == 's' and player == 'w') or \
         (computer == 'w' and player == 'g') or \
         (computer == 'g' and player == 's'):
        comp_win += 1
        print(f"Computer Won round {rounds}\n")
    else:
        user_win += 1
        print(f"You Won round {rounds}\n")

    rounds += 1

# Final winner based on the number of wins
print("Final Result:")
if user_win > comp_win:
    print(f"Congratulations!! You Won ({user_win} - {comp_win})")
elif comp_win > user_win:
    print(f"You Lose!! ({comp_win} - {user_win})")
else:
    print(f"Match Draw!! ({user_win} - {comp_win})")

