from typing import List

def removeElement(nums:List, val:int) -> int:
    for n in nums:
        if n == val:
            nums.pop(n)
        else:
            continue
    return len(nums)


someList = [1, 2, 3, 4, 5, 6, 7]
someVal = 5
print(removeElement(someList, someVal))