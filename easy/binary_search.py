from typing import List

def binary_search(nums: List[int],target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

case_1 = binary_search([-1,0,3,5,9,12], 9)
case_2 = binary_search([-1,0,3,5,9,12], 2)
print(f"caso 1 = {case_1}, caso 2 = {case_2}")