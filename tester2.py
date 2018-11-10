# import sys
#
#
# def is_5b(name):
#     if name == "vignesh":
#         return True
#     else:
#         return False
#
#
# if __name__ == "__main__":
#     name = sys.argv[1]
#     print(is_5b(name))

import json


FILENAME = "votes.json"

def get_votes():
    with open(FILENAME) as file:
        return json.load(file)


def set_votes(votes):
    with open(FILENAME, 'w') as file:
        return json.dump(votes, file, indent=2)


def vote_for(song):
    votes = get_votes()
    votes[song] += 1
    set_votes(votes)

def add_choice(song):
    votes = get_votes()
    votes[song] = 0
    set_votes(votes)
