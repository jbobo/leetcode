#!/usr/bin/env python3

"""TODO: Do the thing.
"""

class Thing:
    """A thing Object.
    """
    list = []

    def __init__(self):
        self.list = []
    
    def get_list(self):
        return self.list
    

if __name__ == "__main__":
    this_thing = Thing()

    list = this_thing.get_list()
    for entry in list:
        print(entry)