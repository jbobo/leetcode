def find_all_substrings(array):
    # initialize with an empty substring.
    previous_substring_list = []
    substring_list = [[]]

    # add the first set of substrings.
    for _, element in enumerate(array):
        if [element] not in previous_substring_list:
            previous_substring_list.append([element])

    substring_list += previous_substring_list

    # loop through the leftover indexes in the given array, creating next "depth" of substrings.
    for _, _ in enumerate(array[1:]):
        new_substring_list = []
        # we want to add each element from the array to the previous set of substrings we made.
        for substring in previous_substring_list:
            for _, element in enumerate(array):
                new_substring = substring + [element]
                # only add unique substrings.
                new_substring.sort()
                if new_substring not in new_substring_list:
                    new_substring_list.append(new_substring)
        # add the new set to our total set of substrings.
        substring_list += new_substring_list
        previous_substring_list = new_substring_list
    return substring_list


if __name__ == "__main__":
    test_array = [1, 2, 1]
    print(find_all_substrings(test_array))
