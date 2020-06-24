#!/usr/bin/env python3


def twosum(input_list, target_val):
    sum_location = {}
    for index, number in enumerate(input_list):
        if number in sum_location:
            return [index, sum_location[number]]
        sum_location[target_val - number] = index
    return []


if __name__ == "__main__":
    input_list = [2, 7, 11, 15]
    target_sum = 9

    twosum = twosum(input_list, target_sum)
    print(twosum)
