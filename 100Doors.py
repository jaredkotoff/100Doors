import random

# Simply picks the winning door at random
def door_picker():
    winner = random.randrange(1, doors+1)
    return winner

# This opens all the other doors and allows the user to swich or stay
def door_opener(choice, winner, switch, enable_auto):
    if enable_auto == "n":
        switch = None
    if choice == winner:
        closed_door = random.randrange(1, doors+1)
        while closed_door == winner:
            closed_door = random.randrange(1, doors+1)
    else:
        closed_door = choice
    print("I have opened all but doors " + str(closed_door) + " and " + str(winner))
    if enable_auto == "n":
        while not (switch == "y" or switch == "n"):
            switch = input("Would you like to switch?(y\\n): ").lower()
    if switch == "y":
        if choice == winner:
            choice = closed_door
        else:
            choice = winner
    return choice, switch

# This is the end game. Displays if the player won or lost
def show_winner(choice, winner, switch):
    if switch == "n":
        print("You did not switch and you ", end="")
    else:
        print("You switched and you ", end="")
    if choice == winner:
        print("won!")
        return 1
    else:
        print("lost.")
        return 0

# Calculates the amount of games won vs played and your % of wins
def show_rate(wins, games):
    rate = wins / games
    print("\n" + str(wins) + " wins of " + str(games) + " games")
    print("You are winning " + str(rate*100) + "% of the time.\n\n")

# Sorry for the mess
# Theres cleaner ways to made this main but I got tired
def main():
    global doors
    doors = "0"
    wins = 0
    games = 0
    total_games = "0"
    switch = "0"
    enable_auto = None
    keep_playing = "y"
    while not (doors.isdigit() and 2 < int(doors)):
        doors = input("How many doors would you like to play with? ")
    doors = int(doors)
    while not (enable_auto == "y" or enable_auto == "n"):
            enable_auto = input("Would you like to see autoplay?(y\\n): ").lower()
    if enable_auto == "y":
        while not (switch == "y" or switch == "n"):
            switch = input("Always switch doors?(y\\n): ")
        while not (total_games.isdigit() and 0 < int(total_games)):
            total_games = input("How many games?: ")
    while keep_playing == "y":
        choice = "0"
        if enable_auto == "y":
            choice = str(random.randrange(1, doors+1))
        print("There are 100 doors in front of you.\nOne contains a prize.\n")
        if enable_auto == "n":
            while not (choice.isdigit() and 0 < int(choice) < doors+1):
                choice = input("Pick one: ")
        winner = door_picker()
        choice, switch = door_opener(int(choice), winner, switch, enable_auto)
        wins += show_winner(int(choice), winner, switch)
        games += 1
        show_rate(wins, games)
        if enable_auto == "n":
            keep_playing = None
            while not (keep_playing == "y" or keep_playing == "n"):
                keep_playing = input("Would you like to keep playing?(y\\n): ").lower()
        elif int(total_games) == games:
            keep_playing = "n"


if __name__ == '__main__':
    main()
