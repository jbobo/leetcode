#! /usr/bin/env

from heapq import heappop, heappush


def topKFrequent(words, count):
    frequency_dict = {}
    word_count = {}
    max_heap = []
    most_frequent_words = []

    if count > len(words):
        return []

    for word in words:
        word_count.setdefault(word, 0)
        word_count[word] += 1

    for word, frequency in word_count.items():
        frequency_dict.setdefault(frequency, [])
        frequency_dict[frequency].append(word)

    for frequency in frequency_dict:
        heappush(max_heap, -1 * frequency)

    while len(most_frequent_words) < count:
        frequency = abs(heappop(max_heap))
        words = frequency_dict[frequency]
        sorted_words = sorted(words)
        most_frequent_words.extend(sorted_words)

    return most_frequent_words


if __name__ == "__main__":
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    count = 2

    top_k_frequent_words = topKFrequent(words, count)

    print(top_k_frequent_words)
