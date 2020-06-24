#!/usr/bin/env python3


def longestPalindromeSubseq(input_string):
    """
    """
    palindrome_length_at = [[1]*len(input_string)
                            for i in range(len(input_string))]

    for length in range(2, len(input_string) + 1):
        for left in range(len(input_string) - length + 1):
            right = left + length - 1
            # IF: current edges are a palindrome.
            if input_string[left] == input_string[right]:
                inner_length = 0
                if length > 2:
                    inner_length = palindrome_length_at[left + 1][right - 1]
                palindrome_length_at[left][right] = inner_length + 2
            # ELSE: try removing left edge OR right edge.
            else:
                remove_left = palindrome_length_at[left + 1][right]
                remove_right = palindrome_length_at[left][right - 1]
                palindrome_length_at[left][right] = max(
                    remove_left, remove_right)

    return(palindrome_length_at[0][-1])


if __name__ == "__main__":
    input_string = "BBABCB"
    max_length = longestPalindromeSubseq(input_string)
    print(max_length)
