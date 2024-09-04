class Solution:
    def decodeString(self, s: str) -> str:
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        res = []
        cur = ""
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                res.append((cur, num))
                cur = ""
                num = 0
            elif char == ']':
                prev, num1 = res.pop()
                cur = prev + num1 * cur
            else:
                cur += char
        return cur
       
