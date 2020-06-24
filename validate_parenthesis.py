#!/usr/bin/env python3


def validate_parens(string):
    matches = {
        "}": "{",
        "]": "[",
        ")": "("
    }
    stack = []
    for char in string:
        if char not in matches:
            stack.append(char)
        else:
            if stack:
                last_open_bracket = stack.pop()
                if last_open_bracket != matches[char]:
                    return False
            else:
                return False
    if stack:
        return False
    return True


if __name__ == "__main__":
    string = "{{([])}}"
    print(validate_parens(string))
