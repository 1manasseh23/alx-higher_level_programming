#!/usr/bin/python3
import random
nums = random.randint(-10, 10)
print(nums, end=" ")
if nums > 0:
    print("is positive")
elif nums == 0:
    print("is zero")
else:
    print("is negative")
