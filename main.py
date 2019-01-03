from webpage import *
from champions import *


def main():
    champion, lane = get_input()

    webpage = get_webpage(champion)

    get_counter_champions(webpage, lane)


def get_input():
    while True:
        input_champion = str(input("Enter a champion name: ")).replace(" ", "")
        input_lane = str(input("Enter lane (top, jungle, mid, adc or supp): "))

        try:
            champion = get_closest_champion(input_champion)
            lane = get_closest_lane(input_lane)
            break
        except IndexError:
            print("Couldn't find any matches to those inputs, try again..")
            continue

    return champion, lane


main()
