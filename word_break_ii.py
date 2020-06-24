#!/usr/bin/env python3


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

    # keys map all found sentences to their start_index
    # { START_INDEX: SENTENCE }
    sentences = {}
    # Add seed value.
    sentences[len(input_string)] = []
    # Backtrack and reconstruct all possible combinations back to index 0.
    # range(len(input_string), 0, -1):
    for end_index in range(len(input_string), -1, -1):
        # There is no matching word that ends on this index, so skip it.
        if end_index not in sentences:
            continue
        # Get all previous sentences that begin at this index.
        sentences_at_end_index = sentences.get(end_index, [])
        # Get all matching words at this index
        for start_index in word_dict_matches.get(end_index, []):
            # Get all valid substrings that come after the matched word.
            sentences_at_start_index = []
            if sentences_at_end_index:
                for end_sentence in sentences_at_end_index:
                    new_sentence = (
                        input_string[start_index: end_index]
                        + " "
                        + end_sentence
                    )
                    sentences_at_start_index.append(new_sentence)
            else:
                # Init for when we are starting a sentence from the end of the input_string
                sentences_at_start_index = [
                    input_string[start_index: end_index]
                ]
            # Add the newly found sentences for this start_index to sentences{}.
            if start_index in sentences:
                sentences[start_index].extend(sentences_at_start_index)
            else:
                sentences[start_index] = (sentences_at_start_index)

    return sentences.setdefault(0, [])


if __name__ == "__main__":
    word_string = "catsanddog"
    word_dict = ["cat", "cats", "and", "sand", "dog"]
    print(word_string)
    print(word_dict)
    print(wordBreak(word_string, word_dict))
