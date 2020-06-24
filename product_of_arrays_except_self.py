#!/usr/bin/python3
"""Given an array nums of n integers where n > 1,  return an array output such
that output[i] is equal to the product of all the elements of nums except
nums[i].
"""


def productExceptSelf(nums):
    length = len(nums)

    products = [0] * length
    products[0] = 1

    # answer[i] contains the product of all the elements to the left
    # Note: for the element at index '0', there are no elements to the left,
    #  so the answer[0] would be 1
    for i in range(1, length):
        products[i] = nums[i-1] * products[i-1]

    # use right to store the product of all elements to the right of i.
    right = 1
    for i in reversed(range(length)):
        products[i] = products[i] * right
        right *= nums[i]

    return products


if __name__ == "__main__":
    input_list = [1, 2, 3, 4]
    products = productExceptSelf(input_list)
    print(products)
