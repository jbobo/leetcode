
def length_of_LUS(input_string):
    """This function takes in a string and returns the int length of the LUS
    (longest unique substring) containing no repeating characters.
    """
    max_length = 0
    current_length = 0

    # use to track the index of each previously parsed char
    duplicate_set = set()

    for i in range(len(input_string)):
        char = input_string[i]
        # check if the current char is a duplicate
        if char in duplicate_set:
            # calculate the length of the current substring without the duplicate
            current_length = 0
            # reset duplicate_set
            duplicate_set.clear()
        duplicate_set.add(char)
        current_length += 1
        # update the max length if the current_length is bigger
        if current_length > max_length:
            max_length = current_length
    
    return max_length


if __name__ == "__main__":
    input_strings = [
        "babcdbaefghijk", # 9
        "aaaa", # 1
        "aabac", # 3
        "abcdefg", # 7
        "" # 0
    ]
    for string in input_strings:
        print("Length of LUS in %s is %s" % (string, length_of_LUS(string)))
