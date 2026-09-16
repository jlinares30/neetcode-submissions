class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visted = {}
        for index, i in enumerate(nums):
            complemento = target - i
            if complemento in visted:
                return [visted[complemento], index]
            else:
                visted[i] = index