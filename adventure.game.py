import time
import random

'''
Text-based adventure game that takes input from player and give them
choices on how to advance throughout the game.
'''


def print_pause(phrase):
    time.sleep(1)
    print(phrase)
    time.sleep(1)
    return


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid. Try again!')
    return


def knockOnDoor(monster):  # pick # 1 knock on Door storyline
    print_pause("You hear a rattle on the door!")
    print_pause(f"It sounds like a {monster}. What do you do?")
    print_pause("Press 3 for running away. Press 4 to open door.")

    answer = valid_input("(Please enter 3 or 4.)", ["3", "4"])

    if (answer == "3"):
        print_pause("You safely got away!")
        return -1
    else:
        print_pause(f"There is a {monster} inside...you can't outrun it.")
        print_pause("You black out as soon as the monster charges at you")
        return -2


def go_cave(monster):  # pick # 2 go to cave Storyline
    print_pause("The cave is dark...you hear something behind you.")
    print_pause(f"It sounds like a {monster}. What do you do?")
    print_pause("Press 3 for running away. Press 4 to turn around.")

    answer = valid_input("(Please enter 3 or 4.)", ["3", "4"])

    if (answer == "3"):
        print_pause("You safely got away!")
        return -1
    else:
        print_pause(f"There is a {monster} behind you...you can't outrun it.")
        print_pause("You black out as soon as the monster charges at you")
        return -2


def play_again():
    choice = valid_input("Play again? [y|n]", ['y', 'n'])
    if choice == 'n':
        print_pause('Thanks for playing! Goodbye!')
        exit(0)
    else:
        play_game()
        return


def play_game():
    playing = True  # game continues true
    ending = 0
    print_pause("Hello. Welcome to the Adventure Game! Read the statements"
                " carefully. And be sure to enter correct inputs.")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave. What would you like to do?"
                "(Please enter 1 or 2).")
    # randomize monster spawned in game
    monsters = ["goblin", "ghoul", "troll", "demon", "monster"]
    pickMonster = monsters[random.randint(0, len(monsters)-1)]

    while(playing):

        answer = valid_input("(Please enter 1 or 2.)", ["1", "2"])
        if (answer == "1"):
            ending = knockOnDoor(pickMonster)
        elif (answer == "2"):
            ending = go_cave(pickMonster)

        if ending == -1:
            print_pause("Congratulations on winning the Adventure Game.")
            print_pause("You are deemed the best gamer in Adventure land.")
            playing = False
        elif ending == -2:
            print_pause("Sorry you lost the Adventure Game! Try Again!")
            playing = False

    play_again()
    return


play_game()
