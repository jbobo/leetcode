#!/usr/bin/env python3

"""Given a set of candidate numbers (candidates) (without duplicates) and a
target number (target), find all unique combinations in candidates where the
candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of
times.
"""


def get_combinations_sum(candidates, target):
    queue = [[]]
    combinations = []
    visited = set()

    while queue:
        current_combo = queue.pop(0)
        for num in candidates:
            new_combo = sorted(current_combo + [num])
            new_sum = sum(new_combo)
            if str(new_combo) not in visited:
                visited.add(str(new_combo))
                if new_sum == target:
                    combinations.append(new_combo)
                elif new_sum < target:
                    queue.append(new_combo)
                elif new_sum > target:
                    continue
    return combinations


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    combinations = get_combinations_sum(candidates, target)
    print(combinations)
