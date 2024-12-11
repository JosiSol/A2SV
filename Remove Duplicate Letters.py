class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        left = Counter(s)
        star = []
        
        w = set()
        for c in s:
            
            while star and c < star[-1] and left[star[-1]] > 0 and c not in w:
                w.remove(star.pop())
            
            if c not in w:
                star.append(c)

            left[c] -= 1
            w.add(c)

        return ''.join(star)
