#!/usr/bin/python3
def canUnlockAll(boxes):
  unlocked = [False] * len(boxes)
  unlocked[0] = True
  for box in boxes:
    for key in box:
      unlocked[key] = True
  return all(unlocked)
