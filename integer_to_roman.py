#!/usr/bin/env python3


def get_nearest_roman_num(num):
    roman_nums = ['M', 'CM', 'D', 'CD', 'C', 'XC',
                  'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    latin_nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    match = 0
    for i in range(len(latin_nums)):
        if latin_nums[i] >= num:
            if latin_nums[i] == num:
                match = i
            elif latin_nums[i+1] < num:
                match = i+1
    return (latin_nums[match], roman_nums[match])


def int_to_roman(num):
    roman_numeral = ""
    while num > 0:
        latin_num, roman_num = get_nearest_roman_num(num)
        roman_numeral += roman_num
        num -= latin_num
    return roman_numeral


if __name__ == "__main__":
    num = 1994
    roman = int_to_roman(num)
    print(num, roman)
