"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    """ checks if the linked list has a cycle """

    if not head or not head.next:
        return head

    all_elements = set()
    current_node = head

    while current_node:
        if current_node.data in all_elements:
            return True
        else:
            all_elements.add(current_node.data)

        current_node = current_node.next

    return False
