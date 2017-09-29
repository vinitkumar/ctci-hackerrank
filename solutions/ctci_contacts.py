""" Tries: Contacts """

class Node(object):
    """ Trie node """

    def __init__(self, letter):
        self.letter = letter
        self.children = set()

    def __str__(self):
        string = self.letter
        string += " ["
        for child in self.children:
            string += child.__str__()
        string += "] "
        return string

def get_node(last_alphabet_node, character):
    """
    @return: a child node of last_alphabet_node with the given character
    if it exists, else creates a new child and returns it
    """
    for child_alphabet in last_alphabet_node.children:
        if character == child_alphabet.letter:
            return child_alphabet

    new_child_alphabet = Node(character)
    last_alphabet_node.children.add(new_child_alphabet)

    return new_child_alphabet

def add_to_trie(trie_root, word):
    """ Function to add a word to the trie """
    last_alphabet_node = trie_root

    for character in word:
        last_alphabet_node = get_node(last_alphabet_node, character)

    return trie_root

def find_in_trie(trie_root, word):
    """ Function to find the count of partial matches
    of a word in a trie """
    pass


def main():
    """ Main fn. """
    n = int(input().strip())

    trie_root = Node('~')

    for _ in range(n):
        operation, word = input().strip().split(' ')

        if operation == "add":
            trie_root = add_to_trie(trie_root, word)
            print(trie_root)
        # elif operation == "find":
        #     count_occurrences = find_in_trie(trie_root, word)

if __name__ == '__main__':
    main()
