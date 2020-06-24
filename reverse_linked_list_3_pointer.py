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
    lead_pointer = None
    mid_pointer = head
    trail_pointer = None

    while mid_pointer:
        # stash the next element
        lead_pointer = mid_pointer.next
        # set the mid pointer to the previous element
        mid_pointer.next = trail_pointer
        # previous is moved up to the current node
        trail_pointer = mid_pointer
        # update the current node from the stashed value
        mid_pointer = lead_pointer
        # lead_pointer = mid_pointer.next

    return trail_pointer


if __name__ == "__main__":
    test_list = ListNode("A", ListNode("B", ListNode("C", ListNode("D"))))
    test_list.print_list()
    reversed_list = reverse_list(test_list)
    reversed_list.print_list()
