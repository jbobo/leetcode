#! /usr/bin/env python3


def wordBreak(input_string, word_dict):
    # Keys map to arrays of indices of all words that end at key index.
    # { END_INDEX: START_INDEX } for all matches from word_dict
    word_dict_matches = {}
    # Add seed value.
    word_dict_matches[0] = []

    # Loop over once to map start_indexes to end_indexes for matching words.
    for index in range(len(input_string)):
        # There are no matching words that lead to this index, so skip it.
        if index not in word_dict_matches:
            continue
        # Instead of storing the entire word, store the start and end indices.
        #   We'll use this to take slices from the input string later and save
        #   space.
        for word in word_dict:
            if input_string.startswith(word, index):
                end_index = index + len(word)
                word_dict_matches.setdefault(end_index, []).append(index)

    # If words can't be formed, return []
    if len(input_string) not in word_dict_matches:
        return []

    # Word Break II starts here, simply do the DFS in words and generate sentences
    stack = []
    stack.append(("", len(input_string)))
    results = []
    while stack:
        sentence, end_index = stack.pop()
        start_index_list = word_dict_matches.get(end_index, [])
        # We are adding spaces, so need to remove them before checking
        #   length, this can probably be improved though.
        for start_index in start_index_list:
            word = input_string[start_index:end_index]
            new_sentence = ""
            if sentence:
                new_sentence = word + " " + sentence
            else:
                new_sentence = word
            if start_index == 0:
                results.append(new_sentence)
            else:
                new_stack_entry = (new_sentence, start_index)
                stack.append(new_stack_entry)
    return results


if __name__ == "__main__":
    input_string = "catsanddog"
    word_dict = ["cat", "cats", "and", "sand", "dog"]
    sentences = wordBreak(input_string, word_dict)
    print(sentences)
