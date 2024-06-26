class Solution:
    def a(self, c):
        return c in ('a','A','e','E','i','I','o','O','u','U')
    
    def reverseVowels(self, s: str) -> str:
        i,j = 0,len(s) - 1
        s = list(s)
        while i < j:
            while i < j and (not self.a(s[i])):
                i += 1
            while i < j and (not self.a(s[j])):
                j -= 1
            if i < j:
                s[i],s[j] = s[j],s[i]
                i += 1
                j -= 1
        return ''.join(s)
        
