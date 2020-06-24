#!/usr/bin/env python3
"""Implement an algorithms that finds the longest palindrome contained as a
substring of hte given input string.
"""


def expand_from_center(string, low, high):
    """ Expand from the given indices to find the longest palindromic substring
    rooted at (low, high).
    """
    palindrome = None
    while (low >= 0 and high < len(string)):
        if string[low] == string[high]:
            print(string[low:high+1])
            palindrome = string[low:high + 1]
            high += 1
            low -= 1
        else:
            break
    return palindrome


def get_longest_palindrome(string):
    """Find the longest palindromic substring contained in the given string.
    """
    longest_palindrome = ""

    for i in range(0, len(string)):
        palindrome = expand_from_center(string, i, i)
        if len(palindrome) > len(longest_palindrome):
            longest_palindrome = palindrome
        if i > 0 and string[i] == string[i - 1]:
            palindrome = expand_from_center(string, i - 1, i)
            if len(palindrome) > len(longest_palindrome):
                longest_palindrome = palindrome

    return longest_palindrome


if __name__ == "__main__":
    test_string = "babad"
    # print(test_string[1:2])
    longest_palindrome = get_longest_palindrome(test_string)
    print(longest_palindrome)
