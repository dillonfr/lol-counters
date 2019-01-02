from exception import ChampionException
from webpage import *
import json

# TODO: Test new functions (test reading from json, test refactored functions)
# TODO: Find closest champion name to string input using difflib


def main():
    champion, lane = get_input()

    webpage = get_webpage(champion)

    get_counter_champions(webpage, lane)


def get_input():
    lanes = ["top", "jungle", "mid", "adc", "supp"]

    while True:
        try:
            champion = str(input("Enter a champion name: ")).replace(" ", "")
            lane = str(input("Enter lane (top, jungle, mid, adc, supp): "))

            if not champion.isalpha():
                raise ChampionException

            if lane not in lanes:
                print("Invalid lane, did you spell it correctly?")
                continue
            else:
                break

        except ChampionException:
            print("Champion names must contain letters and spaces only!")

    return champion, lane


main()
