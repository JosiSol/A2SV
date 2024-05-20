class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        start,end = 0,0
        
        for i, c in enumerate(s):
            start += 1
            end = max(end, lastIndex[c])
            
            if i == end:
                res.append(start)
                start = 0
        
        return res
