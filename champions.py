import difflib
import json


def get_closest_champion(input_name):
    with open('champion_lanes.json') as f:
        champion_lanes = json.load(f)

    all_champion_names = champion_lanes.keys()

    closest_matches = difflib.get_close_matches(input_name, all_champion_names, 10, 0.2)

    for name in closest_matches:
        if name.startswith(input_name):
            best_match = name
            break
    else:
        best_match = closest_matches[0]

    return best_match


def get_closest_lane(input_lane):
    lanes = ["top", "jungle", "mid", "adc", "supp"]

    closest_matches = difflib.get_close_matches(input_lane, lanes, 5, 0.2)

    best_match = closest_matches[0]

    return best_match
