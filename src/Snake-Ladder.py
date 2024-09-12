import random

def ladder_game(num_players, size):
    players = [0] * num_players  # Initialize player positions to 0

    def roll_dice():
        # Generate a random number between 1 and 6
        return random.randint(1, 6)

    while True:
        for i in range(num_players):
            input(f"\nPlayer {i + 1}, press Enter to roll the dice: ")
            roll = roll_dice()
            print(f"Player {i + 1} rolled a {roll}")
            players[i] += roll


            # Check if the player has reached the last box
            if players[i] >= size**2:
                print(f"Player {i + 1} has won!")
                return

            print(f"Player {i + 1} is now at position {players[i]}")

if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))
    size = int(input("Enter the number of boxes: "))
    ladder_game(num_players, size)