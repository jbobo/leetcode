#!/usr/bin/env python3
from string import ascii_lowercase


def get_neighbors(word, word_set):
    for index in range(len(word)):
        for char in ascii_lowercase:
            if char == word[index]:
                continue
            neighbor = word[:index] + char + word[index + 1:]
            if neighbor in word_set:
                yield neighbor


def findLadders(begin_word, end_word, word_list):
    word_set = set(word_list)

    # validate
    if end_word not in word_set:
        return []

    queue = []
    queue.append((begin_word, 0))

    word_depth = {}  # { word: depth}
    graph = {}  # { word: [neighboring words]}
    visited = {begin_word}

    # BFS to build adjacency matrix and map word depths.
    while queue:
        word, distance = queue.pop(0)
        word_depth[word] = distance
        for neighbor in get_neighbors(word, word_set):
            graph.setdefault(word, set()).add(neighbor)
            # graph.setdefault(neighbor, set()).add(word)
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))
                visited.add(neighbor)

    if end_word not in visited:
        return []

    path_list = []
    stack = [[begin_word]]

    # DFS to find paths
    while stack:
        path = stack.pop()
        word = path[-1]
        if word == end_word:
            path_list.append(path)
            continue
        current_depth = word_depth[word]
        for neighbor in graph.get(word, []):
            if word_depth[neighbor] > current_depth:
                stack.append(path + [neighbor])

    return path_list


if __name__ == "__main__":
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]

    ladders = findLadders(begin_word, end_word, word_list)

    print(begin_word, end_word, word_list)
    print(ladders)
