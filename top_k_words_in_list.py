#!/usr/bin/env python3


def get_top_k_strings(words, count):
    """
    """
    frequency_dict = {}
    word_count = {}
    most_frequent_words = []

    if count > len(words):
        return None

    for word in words:
        word_count.setdefault(word, 0)
        word_count[word] += 1

    for word, frequency in word_count.items():
        frequency_dict.setdefault(frequency, [])
        frequency_dict[frequency].append(word)

    while len(most_frequent_words) < count:
        max_frequency = max(frequency_dict)
        sorted_words = frequency_dict.pop(max_frequency)
        sorted_words.sort()
        most_frequent_words.extend(sorted_words)

    return most_frequent_words[0:count]


if __name__ == "__main__":
    word_list = ["i", "love", "leetcode", "i", "love", "coding"]
    count = 2
    print(get_top_k_strings(word_list, count))
