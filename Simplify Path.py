class Solution:
    def simplifyPath(self, path: str) -> str:
        #Time Complexity = O(3n) = O(n)
        #Space Complexity = O(2n) = O(n)
        stack = []
        for p in path.split('/'):
            if p == "" or p == '.':
                continue
            if p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return '/' + '/'.join(stack)
