""" Tries: Contacts """

class Node(object):
    """ Trie node """

    def __init__(self, letter):
        self.letter = letter
        self.children = set()
        self.terminating_words_count = 1

    def __str__(self):
        string = self.letter + "(" + str(self.terminating_words_count) + ")"
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
            child_alphabet.terminating_words_count += 1
            return child_alphabet

    new_child_alphabet = Node(character)
    last_alphabet_node.children.add(new_child_alphabet)

    return new_child_alphabet

def add_to_trie(trie_root, word):
    """ Function to add a word to the trie """
    last_alphabet_node = trie_root

    for character in word:
        last_alphabet_node = get_node(last_alphabet_node, character)
    last_alphabet_node = get_node(last_alphabet_node, '$')

    return trie_root

def count_possible_words(current_characters, current_count):
    """
    Given a set of characters and a count of terminating words
    find the number of terminating words
    """

    if not current_characters:
        return current_count

    non_terminating_nodes = set()
    for charnode in current_characters:
        if charnode.letter == '$':
            current_count += 1
        else:
            for child in charnode.children:
                non_terminating_nodes.add(child)

    return count_possible_words(non_terminating_nodes, current_count)


def find_in_trie(trie_root, word):
    """ Function to find the count of partial matches
    of a word in a trie """

    current_characters = trie_root.children
    trie_character = None
    for character in word:
        # print("current_word_character: ", character)
        children_matched = False
        for trie_character in current_characters:
            # print("current_trie_character: ", trie_character.letter)
            if character == trie_character.letter:
                children_matched = True
                current_characters = trie_character.children
                break

        if not children_matched:
            return 0

    if trie_character:
        return trie_character.terminating_words_count
    else:
        return 0


def main():
    """ Main fn. """
    num_ops = int(input().strip())

    trie_root = Node('~')

    for _ in range(num_ops):
        operation, word = input().strip().split(' ')

        if operation == "add":
            trie_root = add_to_trie(trie_root, word)
            # print(trie_root)
        elif operation == "find":
            count_occurrences = find_in_trie(trie_root, word)
            print(count_occurrences)

if __name__ == '__main__':
    main()
