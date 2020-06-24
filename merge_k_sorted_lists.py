#!/usr/bin/env python3
""" Implement an algorithm to merge K sorted linked lists.

This solution pushes each node value into a min-heap/p-queue and then pushes each
value from the heap into a new sorted linked list
"""
from heapq import heappush, heappop


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists):
    min_heap = []

    for node in lists:
        while node:
            heappush(min_heap, node.val)
            node = node.next
    if min_heap:
        sorted_list_head = ListNode(heappop(min_heap))
        pointer = sorted_list_head
        while min_heap:
            pointer.next = ListNode(heappop(min_heap))
            pointer = pointer.next
        return sorted_list_head
    return None


if __name__ == "__main__":
    # [[1,4,5],[1,3,4],[2,6]]
    lists = [
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6))
    ]
    merged_list = merge_k_lists(lists)
    while merged_list:
        print(merged_list.val)
        merged_list = merged_list.next
