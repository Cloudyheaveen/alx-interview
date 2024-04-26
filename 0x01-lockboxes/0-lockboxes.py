#!/usr/bin/python3
"""Script will unlock list of lists"""

def canUnlockAll(boxes):
    keys = [0]  # Start with the key to the first box
    for key in keys:
        # Iterate through the keys in the current box
        for boxKey in boxes[key]:
            # If the key unlocks a new box and the box exists
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)  # Add the new key to the list of keys
    return len(keys) == len(boxes)  # Check if all boxes can be opened

