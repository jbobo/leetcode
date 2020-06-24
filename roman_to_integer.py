#!/usr/bin/env python3


def roman_to_int(roman_string):
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    total = 0

    i = 0
    while i < len(roman_string):
        current_num = roman_dict[roman_string[i]]
        if i < (len(roman_string) - 1):
            next_num = roman_dict[roman_string[i+1]]
            if current_num < next_num:
                total += (next_num - current_num)
                i += 2
                continue

        total += current_num
        i += 1

    return total


if __name__ == "__main__":
    roman = "CMXCIV"  # 994

    integer = roman_to_int(roman)
    print(integer)
