#!/usr/bin/env python3
"""Alice walks from point A to point B,

"""
from math import gcd


# def gcd(x, y):
#     while(y):
#        x, y = y, x % y
#
#     return x


def lattice(first_x, first_y, second_x, second_y):
    delta_x = second_x - first_x
    delta_y = second_y - first_y

    # rotate 90: (x, y);
    #   clockwise => (y, -x);
    #   counterclockwise => (-y, x);
    rotated_delta_x = delta_y
    rotated_delta_y = -(delta_x)

    # get the GCD of the rotated point.
    gcd_x_y = abs(gcd(rotated_delta_x, rotated_delta_y))
    reduced_rotated_delta_x = rotated_delta_x / gcd_x_y
    reduced_rotated_delta_y = rotated_delta_y / gcd_x_y

    # add second x and y to rotated x and y, respectively.
    third_x = second_x + reduced_rotated_delta_x
    third_y = second_y + reduced_rotated_delta_y

    return (third_x, third_y)


if __name__ == "__main__":
    pass
