# /usr/bin/env python3


def threeSum(nums, target_sum=0):
    # sort the input_list.
    nums.sort()
    three_sum_list = []
    three_sum_set = set()

    # check empty list; lowest sum > target; max sum < target;
    if (not nums) or sum(nums[0:3]) > target_sum or sum(nums[len(nums)-3:len(nums)]) < target_sum:
        return []

    for low in range(len(nums)):
        mid, high = low + 1, len(nums)-1
        while low < mid < high:
            # Skip duplicate entries.
            if low > target_sum and nums[low] == nums[low-1]:
                break

            current_sum = nums[low] + nums[mid] + nums[high]
            current_sum_tuple = (nums[low], nums[mid], nums[high])

            if current_sum == target_sum and current_sum_tuple not in three_sum_set:
                three_sum_set.add(current_sum_tuple)
                three_sum_list.append(current_sum_tuple)
            elif current_sum < target_sum:
                mid += 1
            elif current_sum >= target_sum:
                high -= 1
    return three_sum_list


if __name__ == "__main__":
    list = [-1, 0, 1, 2, -1, -4]
    print(threeSum(list))
