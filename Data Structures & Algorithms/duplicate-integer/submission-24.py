class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        apper = {}
        for i in nums:
            if i in nums:
                apper[i] = apper.get(i,0)+1
                if apper[i] > 1: 
                    return True
        return False