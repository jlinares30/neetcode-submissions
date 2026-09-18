class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        visted={}
        for number in nums:
            if number not in visted:
                visted[number] = 1
            else:
                visted[number] += 1
        result = sorted(visted,key=visted.get, reverse=True)[0:k]
        return result