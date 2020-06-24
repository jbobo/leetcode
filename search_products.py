#!/usr/bin/env python3
"""implement a word search using a  search trie.
"""


class Node:

    def __init__(self, val=None, end_of_word=False):
        self.val = val
        self.children = {}
        self.end_of_word = end_of_word


class Trie:

    def __init__(self):
        self.root = Node()

    def add_word(self, word):
        current_node = self.root
        for char in word:
            current_node = current_node.children.setdefault(char, Node(char))
        current_node.end_of_word = True

    def get_n_matches(self, search_word, match_count=3):
        matches = []
        current_node = self.root
        for char in search_word:
            current_node = current_node.children.get(char, False)
            if not current_node:
                return None
        # get top n resulting children
        # while len(matches) <= match_count:
        # dfs from here to find n words.
        stack = [(current_node, search_word)]
        while stack:
            current_node, current_word = stack.pop()
            if current_node.end_of_word:
                matches.append(current_word)
                if len(matches) == match_count:
                    return matches
            for child in sorted(current_node.children, reverse=True):
                child_node = current_node.children[child]
                child_word = current_word + child_node.val
                entry = (child_node, child_word)
                stack.append(entry)
        return matches


def get_suggested_products(products, search_word):
    matches = []
    search_trie = Trie()
    for product in products:
        search_trie.add_word(product)
    current_search_word = ""
    for char in search_word:
        current_search_word += char
        matches.append(search_trie.get_n_matches(current_search_word))
    return matches


if __name__ == "__main__":
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    search_word = "mouse"

    suggested_products = get_suggested_products(products, search_word)
    print(suggested_products)
