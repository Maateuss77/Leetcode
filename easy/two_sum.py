from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if  nums[i] + nums[j] == target:
                    return [i,j]
    return []

case_1 = two_sum([2,7,11,15], 9)
case_2 = two_sum([3,2,4], 6)
case_3 = two_sum([3,3], 6)
print(f"caso 1 = {case_1}, caso 2 = {case_2}, caso 3 = {case_3}")


def two_sum2(nums: List[int], target: int) -> List[int]:
    map = {}
    for idx , i  in enumerate(nums):
        diff = target - i
        if diff in map:
            return [map[diff], idx]
        map[i] = idx
    return []

case_1_2 = two_sum2([2,7,11,15], 9)
case_2_2 = two_sum2([3,2,4], 6)
case_3_2 = two_sum2([3,3], 6)
print(f"caso 1 = {case_1_2}, caso 2 = {case_2_2}, caso 3 = {case_3_2}")
