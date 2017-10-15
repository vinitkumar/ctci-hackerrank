''' Sorting: Comparator '''

from functools import cmp_to_key


class Player(object):
    ''' Player object containing name and score '''

    def __init__(self, name, score):
        pass

    def __repr__(self):
        pass

    def comparator(self, player_1, player_2):
        ''' Custom comparator '''
        pass


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
