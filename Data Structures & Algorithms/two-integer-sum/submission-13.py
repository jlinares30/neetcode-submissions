class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pivot = 0
        for indexi, i in enumerate(nums):
            pivot = i
            for indexj, j in enumerate(nums[indexi+1:], start=indexi+1):
                if pivot + j == target:
                    return [indexi, indexj]

