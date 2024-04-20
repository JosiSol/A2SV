class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,res = 0,0
        dict1 = {}

        for r in range(len(s)):
            dict1[s[r]] = 1 + dict1.get(s[r],0)
            while (r - l + 1) - max(dict1.values()) > k:
                dict1[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res
