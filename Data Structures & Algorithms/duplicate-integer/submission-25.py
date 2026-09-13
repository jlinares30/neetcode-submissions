class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        apper = {}
        for i in nums:
            if i in apper:
                return True 
            apper[i] = True
        return False 