""" Hash Tables: Ransom Note """

from collections import Counter


def ransom_note(magazine, ransom):
    """ Determines if the magazine contains words to write the ransom note """

    magazine_multiset = Counter(magazine)
    note_multiset = Counter(ransom)
    multiset_diff = note_multiset - magazine_multiset

    return len(multiset_diff) == 0


def main():
    """ Main function """

    map(int, input().strip().split(' '))

    magazine = input().strip().split(' ')
    ransom = input().strip().split(' ')
    answer = ransom_note(magazine, ransom)

    answer_str = "Yes" if answer else "No"
    print(answer_str)


if __name__ == '__main__':
    main()
