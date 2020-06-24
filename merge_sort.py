#!/usr/bin/env python3


def merge_sort(input_list):
    if len(input_list) > 1:
        middle = len(input_list) // 2
        print(input_list[:middle])
        left = merge_sort(input_list[:middle])
        right = merge_sort(input_list[middle:])

        sorted_list = []

        while left or right:
            if left and right:
                if left[0] <= right[0]:
                    sorted_list.append(left.pop(0))
                else:
                    sorted_list.append(right.pop(0))
            elif left:
                sorted_list.append(left.pop(0))
            elif right:
                sorted_list.append(right.pop(0))
            else:
                break
        return sorted_list
    else:
        return input_list


if __name__ == "__main__":
    unsorted_list = [12, 11, 13, 5, 6, 7]
    sorted_list = merge_sort(unsorted_list)
    print(sorted_list)
