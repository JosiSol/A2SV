class Solution:
    def isValid(self, s: str) -> bool:
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        stack = []
        association = {')':'(','}':'{',']':'['}
        opening = set(['(', '{', '['])

        for par in s:
            if par in opening:
                stack.append(par)
            else:
                if stack and stack[-1] == association[par]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
