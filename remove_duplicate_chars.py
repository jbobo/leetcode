#!/usr/bin/env python3

def length_of_LUS(input_string):
    """This function takes in a string and returns the int length of the LUS
    (longest unique substring) containing no repeating characters.
    """
    current_start = 0
    max_length = 0
    current_length = 0

    # use to track the index of each previously parsed char
    duplicates = {}

    for i in range(len(input_string)):
        char = input_string[i]
        # check if the current char is a duplicate
        if char in duplicates:
            # check if the duplicate in the current substring
            if duplicates[char] >= current_start:
                # move the pointer past the duplicate
                current_start = duplicates[char] + 1
                # calculate the length of the current substring without the duplicate
                current_length = i - current_start
            # update the char index
            duplicates[char] = i
        else:
            # add the char index
            duplicates[char] = i

        current_length += 1
        # update the max length if the current_length is bigger
        if current_length > max_length:
            max_length = current_length
    
    return max_length

if __name__ == "__main__":
    input_strings = [
        "babcdbaefghijk", # 11
        "aaaa", # 1
        "aabac", # 3
        "abcdefg", # 7
        "" # 0
    ]
    for string in input_strings:
        print("Length of LUS in %s is %s" % (string, length_of_LUS(string)))
