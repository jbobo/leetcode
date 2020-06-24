#!/usr/bin/env python3


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


def reverse_list(head):
    # TODO: do the thing.
    pointer = None

    while head:
        """
        A->B->C->NULL
        lead = A
        trail = NULL
        """
        # lead = A->NULL
        # trail = B->C->NULL
        head.next, pointer = pointer, head.next
        # lead = B->C->NULL
        # trail = A->NULL
        head, pointer = pointer, head

    return pointer


if __name__ == "__main__":
    test_list = ListNode("A", ListNode("B", ListNode("C", ListNode("D"))))
    test_list.print_list()
    reversed_list = reverse_list(test_list)
    reversed_list.print_list()
