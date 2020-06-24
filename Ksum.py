#!/usr/bin/env python3


def get_ksum(input_list, target_val, k=3):

    def twosum(input_list, target_val):
        sums = []
        sum_location = {}
        for number in input_list:
            if number in sum_location:
                sums.append([sum_location[number], number])
            sum_location[target_val - number] = number
        return sums

    def ksum(input_list, target_val, k):
        sums = []
        if k >= 3:
            k_minus_one = k - 1
            for index in range(len(input_list) - k_minus_one):
                if input_list[index] == input_list[index - 1]:
                    continue
                new_target = target_val - input_list[index]
                k_minus_one_sum = ksum(
                    input_list[index + 1:],
                    new_target,
                    k_minus_one
                )
                if k_minus_one_sum:
                    current_val = input_list[index]
                    for values in k_minus_one_sum:
                        sums.append([current_val] + values)
                else:
                    continue
            return sums

        if k == 2:
            return twosum(input_list, target_val)

    input_list.sort()
    # validate min and max sums.
    if not input_list or sum(input_list[:k]) > target_val or sum(input_list[-k:]) < target_val:
        return []

    return ksum(input_list, target_val, k)


if __name__ == "__main__":
    input_list = [-1, 0, -1, 2, 1, -4, 0]
    target_val = 0
    sum_length = 5
    print(get_ksum(input_list, target_val, sum_length))
