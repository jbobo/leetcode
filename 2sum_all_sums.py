#!/usr/bin/env python3


def twosum(input_list, target_val):
    res = []
    lo = 0
    hi = len(input_list) - 1
    while (lo < hi):
        sum = input_list[lo] + input_list[hi]
        if sum < target_val or (lo > 0 and input_list[lo] == input_list[lo - 1]):
            lo += 1
        elif sum > target_val or (hi < len(input_list) - 1 and input_list[hi] == input_list[hi + 1]):
            hi -= 1
        else:
            res.append([input_list[lo], input_list[hi]])
            lo += 1
            hi -= 1
    return res


if __name__ == "__main__":
    input_list = [2, 7, 11, 15]
    target_sum = 9

    twosum = twosum(input_list, target_sum)
    print(twosum)
