#!/usr/bin/env
"""Reverse a linked list from the n-th place to m-th place. Leaving the rest of
the list untouched.
"""


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def print_list(self):
        pointer = self
        print(pointer.val)

        while pointer.next:
            pointer = pointer.next
            print(pointer.val)


def reverse_list(head, start, end):
    """TODO: Reverse the linked list within the given partition.
    The partition is inclusive of the start and end.

    Validations: 0 <= start < end <= len(linked_list)
    """
    tail_pointer = None
    connecting_pointer = None
    previous_pointer = None
    current_pointer = head

    # get to the start index
    for _ in range(start):
        previous_pointer = current_pointer
        current_pointer = current_pointer.next

    # we'll use tail as the new tail of our reversed partition when we're done.
    tail_pointer = current_pointer
    # we'll use this pointer to attach the head of our reversed partition.
    connecting_pointer = previous_pointer

    for _ in range(start, end + 1):
        current_pointer.next, previous_pointer = previous_pointer, current_pointer.next
        current_pointer, previous_pointer = previous_pointer, current_pointer

    # reconnect our reversed partition.
    if connecting_pointer:
        connecting_pointer.next = previous_pointer
    else:
        head = previous_pointer
    tail_pointer.next = current_pointer

    return head


if __name__ == "__main__":
    test_list = ListNode("A", ListNode("B", ListNode("C", ListNode("D"))))
    test_list.print_list()
    reversed_list = reverse_list(test_list, 1, 2)
    reversed_list.print_list()
