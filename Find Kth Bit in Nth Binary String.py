class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        #Time Complexity: O(2^n)
        #Space Complexity: O(n)
        def rev(s):
            t = ''
            for n in s[::-1]:
                if n == '0':
                    t += '1'
                else:
                    t += '0'
            return t
        

        def sn(n):
            if n == 1:
                return '0'
            s = sn(n-1)
            return s + '1' + rev(s)
        

        return sn(n)[k - 1]
        
