class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        so = list()
        l,r = 0,0
        
        for i in range(len(s)):
            if r < len(spaces) and l == spaces[r]:
                so.append(" ")
                r += 1

            so.append(s[i])
            l += 1
        return "".join(so)
