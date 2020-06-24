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
    lead_pointer = head
    trail_pointer = None

    while lead_pointer:
        """
        A->B->C->NULL
        lead = A
        trail = NULL
        """
        # lead = A->NULL
        # trail = B->C->NULL
        lead_pointer.next, trail_pointer = trail_pointer, lead_pointer.next
        # lead = B->C->NULL
        # trail = A->NULL
        lead_pointer, trail_pointer = trail_pointer, lead_pointer

    return trail_pointer


if __name__ == "__main__":
    test_list = ListNode("A", ListNode("B", ListNode("C", ListNode("D"))))
    test_list.print_list()
    reversed_list = reverse_list(test_list)
    reversed_list.print_list()
