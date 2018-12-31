from webpage import *
from exception import ChampionException


# TODO: Write JSON file with champion names and their lanes
# TODO: Test new functions (test reading from json, test refactored functions)
# TODO: Find closest champion name to string input using difflib


def main():
    champion = get_input()

    webpage = get_webpage(champion)

    get_counter_champions(webpage)


def get_input():
    while True:
        try:
            champion = str(input("Enter a champion name: ")).replace(" ", "")

            if not champion.isalpha():
                raise ChampionException

            break

        except ChampionException:
            print("Champion names must contain letters only!")

    return champion


main()
