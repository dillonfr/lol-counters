from exception import ChampionException
from webpage import *
import json

# TODO: Test new functions (test reading from json, test refactored functions)
# TODO: Find closest champion name to string input using difflib


def main():
    champion = get_input()

    webpage = get_webpage(champion)

    get_counter_champions(webpage)

    with open('champion_lanes.json') as f:
        lanes = json.load(f)

    print(lanes["aatrox"]) # gets the lanes aatrox can be played in ["top", "mid", "jungle"]

    if "mid" in lanes["karthus"]:
        print("found")


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
