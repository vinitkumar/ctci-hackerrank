""" Making anagrams """

from collections import Counter


def number_needed(string_1, string_2):
    """ Calculates edit distance to make 2 strings anagrams """

    multiset_1 = Counter(string_1)
    multiset_2 = Counter(string_2)

    all_characters = set(string_1) | set(string_2)
    for character in all_characters:
        count_1 = multiset_1[character]
        count_2 = multiset_2[character]
        multiset_1[character] -= count_2
        multiset_2[character] -= count_1

    edit_distance = 0
    for frequency in list(multiset_1.values()) + list(multiset_2.values()):
        if frequency > 0:
            edit_distance += frequency

    return edit_distance


def main():
    """ Main function """

    string_1 = input().strip()
    string_2 = input().strip()

    print(number_needed(string_1, string_2))


if __name__ == '__main__':
    main()
