#!/usr/bin/python3
"""
Solution to lockboxes problem
"""
def canUnlockAll(boxes):
  """
  Determines whether a series of locked boxes can be opened
  based on keys that can be attained.
  Solution to the lockboxes problem
  """
  if(type(boxes) is not list or len(boxes) == 0):
    return False

  unlocked = [False] * len(boxes)
  unlocked[0] = True
  for box in boxes:
    for key in box:
      unlocked[key] = True
  return all(unlocked)
