''' Sorting: Comparator '''

import json
from functools import cmp_to_key


class Player(object):
    ''' Player object containing name and score '''

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        object_dict = {
            "name": self.name,
            "score": self.score
        }
        return json.dumps(object_dict)

    @staticmethod
    def comparator(player_1, player_2):
        ''' Custom comparator '''
        if player_1.score > player_2.score:
            return -1

        if player_1.score < player_2.score:
            return 1

        if player_1.name < player_2.name:
            return -1

        if player_1.name > player_2.name:
            return 1

        return 0


def main():
    ''' Main function '''

    player_count = int(input())
    data = []
    for i in range(player_count):
        name, score = input().split()
        score = int(score)
        player = Player(name, score)
        data.append(player)

    data = sorted(data, key=cmp_to_key(Player.comparator))
    for i in data:
        print(i.name, i.score)

if __name__ == '__main__':
    main()
