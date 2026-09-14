class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            apper1 = {}
            apper2 = {}
            for i in s:
                apper1[i] = apper1.get(i,0)+1
            for j in t:
                apper2[j] = apper2.get(j,0)+1
            
            return apper1 == apper2
        return False