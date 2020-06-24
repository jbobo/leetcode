#!/usr/bin/env python3
from heapq import heappop, heappush


def get_most_requested_features(features, feature_requests, target_count):
    """TODO: Do the thing.
    """
    top_features = []
    frequency_heap = []

    print(heappush(frequency_heap, (1, "A")))

    return top_features


if __name__ == "__main__":
    features = ["one", "two", "three", "four"]
    feature_requests = [
        "I want oNe",
        "one and two are great",
        "I wish three could do four",
        "TWO would really enable me to do One"
    ]
    target_count = 3

    most_requested_features = get_most_requested_features(
        features, feature_requests, target_count)
    print(most_requested_features)
