#!/usr/bin/env python3


def search(nums, target):
    pivot_index = 0
    list_len = len(nums)

    for i in range(1, len(nums)):
        if nums[i-1] > nums[i]:
            pivot_index = i
            break
    # print("Pivot index found: %s"%(pivot_index))

    min_index = 0
    max_index = list_len - 1

    while min_index <= max_index:
        current_index = (min_index + ((max_index - min_index) // 2))
        rotated_index = ((current_index + pivot_index) % list_len)
        # print("Current index: %s; Rotated index: %s;"%(current_index, rotated_index))
        if nums[rotated_index] == target:
            return rotated_index
        elif nums[rotated_index] < target:
            min_index = current_index + 1
        elif nums[rotated_index] > target:
            max_index = current_index - 1

    return -1


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    target_index = search(nums, target)
    print(target_index)
