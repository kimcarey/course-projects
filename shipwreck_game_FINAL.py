import time
import random


def print_sleep(message_to_print):
    print(message_to_print)
    time.sleep(2)


def game_intro():
    print_sleep("Shipwreck!")
    print_sleep("You wash up on shore, alone.")
    print_sleep("There's nothing but miles of sand and rows of thick,"
                " lush trees.. and a dark cave to your right.")
    print_sleep("You have nothing except your handy pocket knife.")
    print_sleep("All is quiet...then suddenly, you hear a sound.")
    print_sleep("Footsteps!")
    print_sleep("Someone else is on the island...\n")
    print_sleep("What's your next move?")


def game_win():
    print_sleep("GAME OVER. You win!")


def game_lose():
    print_sleep("GAME OVER. You lose!")


# Things that happen if you choose cave
def cave():
    # Random events after selecting "1" for cave
    cave_1 = """Someone else in the cave: "INTRUDER!" You’ve been captured."""

    cave_2 = """You remain quiet until the pirates are out of sight. When all
    is clear, you emerge. You learn to fish and forage for food. You build
    shelter, and crown yourself ruler of the desert island."""

    cave_list = [cave_1, cave_2]
    cave_index = random.choice(range(0, len(cave_list)))

    print_sleep("You run towards the cave.")
    print_sleep("Surrounded by darkness, you wait.")
    if cave_index == 0:
        print_sleep(cave_list[0])
        game_lose()
    if cave_index == 1:
        print_sleep(cave_list[1])
        game_win()


# Things that happen if you choose forest
def forest():
    print_sleep("You take a deep breath and approach the forest, pocket "
                "knife in hand.")
    print_sleep("You see a menacing pirate who is very surprised to see you.")


def forest_question():
    options = [
        "to fight",
        "to surrender"
    ]
    response = ask_choice(options)
    if response == 0:
        print_sleep("You pull out your pocket knife and attack.")
        print_sleep("Victorious, you seize the pirate's food, treasure, "
                    "and ship.\n")
        game_win()
    if response == 1:
        print_sleep("You're taken as prisoner and forced to walk the "
                    "plank, matey!")
        game_lose()


def ask_choice(options):
    question_string = ""
    number_list = list(range(len(options)))
    for n in number_list:
        option_string = options[n]
        question_string += "Enter {} {}\n".format(n, option_string)

    # Keep asking for a choice until they provide a valid
    # option number.
    choice = -1
    while choice not in number_list:
        choice = input(question_string)
        # checks to see if string is a digit
        if choice.isdigit():
            choice = int(choice)
        if choice not in number_list:
            print_sleep("Sorry, I don't understand.")
    return choice


def ask_replay():
    options = [
        "to play again",
        "to quit"
    ]
    response = ask_choice(options)
    if response == 1:
        print_sleep("Heave ho! Sorry to see you go.")
        return False
    elif response == 0:
        print_sleep("Shiver me timbers! Ye gets another chance.")
        return True


def hide_or_approach_question():

    options = [
        "to hide in the cave",
        "to approach the footsteps"
    ]
    response = ask_choice(options)
    if response == 0:
        cave()
    elif response == 1:
        forest()
        forest_question()
    return None


def game_loop():
    while True:
        game_intro()  # tell user about scenario
        hide_or_approach_question()  # ask them to make a choice and execute
        keep_playing = ask_replay()  # ask if they want to play again.
        if keep_playing is False:
            break


#
#
#
game_loop()
