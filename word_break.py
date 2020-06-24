#! /usr/bin/env python3


def wordBreak(input_string, word_dict):
    dictionary = {}
    # Map { end_index: start_index } for matches from word_dict
    dictionary[0] = []

    # Loop through the input_string
    for index in range(len(input_string)):
        # Skip indexes that don't have matches pointing to them.
        if index not in dictionary:
            continue

        # Check if the current index holds any matches.
        for word in word_dict:
            # IF: we find a match, map its ind_index to this start_index in dictionary.
            if input_string[index:].startswith(word):
                end_index = index + len(word)
                # IF: we've found a match linking back to the end of the input_string, return True.
                if end_index == len(input_string):
                    return True
                # ELSE: map the end index to this start index so we can search there later.
                dictionary.setdefault(end_index, []).append(index)

    return False


if __name__ == "__main__":
    input_string = "leetcode"
    word_dict = ["leet", "code"]
    print(wordBreak(input_string, word_dict))
