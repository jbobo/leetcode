#!/usr/bin/env python3
""" Implementation of an LDU cache using a linkedHashMap.
"""


class Node:

    def __init__(self, key=None, val=None, next=None, prev=None):
        self.val = val
        self.key = key
        self.frequency = 1
        self.next = next
        self.prev = prev

    def __str__(self):
        return("Node: Key: %s; Val: %s" % (self.key, self.val))


class DoublyLinkedList:

    def __init__(self):
        self.head = None  # LFU
        self.tail = None  # MFU
        self.length = 0

    def push(self, node):
        """Add a node with the given key and value to the head of the list.
        """
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.length += 1
        return node

    def pop(self, node=None):
        """Remove the given node from the list.
        """
        if not node:  # remove the LRU node
            node = self.tail
        else:
            if node == self.tail:  # node is self.tail
                if node == self.head:  # single node list
                    self.tail = None
                    self.head = None
                elif node.prev:  # length > 1
                    self.tail = node.prev
                    node.prev.next = None
                    node.prev = None
                    # if not self.tail.prev
            elif node == self.head:  # node is self.head
                self.head = node.next
                node.next.prev = None
                node.next = None
            else:  # a middle node in a multi-node list
                node.prev.next = node.next
                node.next.prev = node.prev
                node.next = None
                node.prev = None
            self.length -= 1
        return node


class LFU_cache:

    def __init__(self, capacity):
        # add a sentinel value to seed the cache
        self.node_dict = {}
        self.node_list = DoublyLinkedList()
        self.capacity = capacity

    def get(self, key):
        node = self.node_dict.get(key, None)
        if node:
            # TODO: increment frequency and move up until it's in a nondecreasing spot
            node.frequency += 1
            while node.next and node.frequency >= node.next.frequency:
                temp_node = node.next
                if node.next.next:  # node is not the tail
                    node.next = temp_node.next
                    node.next.prev = node
                else:  # push the node as the new tail
                    self.node_list.tail = node
                    # TODO

                if node.prev:  # node is not the head
                    temp_node.prev = node.prev
                    node.prev.next = temp_node
                else:
                    self.node_list.head = node
                    # TODO
                temp_node.next = node
                node.prev = temp_node

        return node

    def put(self, key, val):
        node = self.node_dict.get(key, None)
        if not node:
            if self.node_list.length >= self.capacity:
                popped_node = self.node_list.pop()
                self.node_dict.pop(popped_node.key)
            node = Node(key, val)
            self.node_dict[key] = node
            self.node_list.push(node)
        elif node.val != val:
            node.val = val
        else:
            return node


if __name__ == "__main__":
    lru = LFU_cache(2)
    print("Put: 0, 0")
    lru.put(0, 0)
    print("Put: 1, 1")
    lru.put(1, 1)
    print("Get: 0: %s" % (lru.get(0)))
    print("Get: 1: %s" % (lru.get(1)))
    print("Put: 2, 2")
    lru.put(2, 2)
    print("Get: 0: %s" % (lru.get(0)))
    print("Get: 1: %s" % (lru.get(1)))
    print("Get: 2: %s" % (lru.get(2)))
