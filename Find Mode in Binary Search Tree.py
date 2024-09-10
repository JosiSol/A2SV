# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        res = []
        if not root:
            return []
        def dfs(r):
            nonlocal res
            if not r:
                return 
            dfs(r.left)
            res.append(r.val)
            dfs(r.right)


        dfs(root)
        freq = Counter(res)
        ababa = max(freq.values())
        lambadina = []
        for i,j in freq.items():
            if j == ababa:
                lambadina.append(i)
        return lambadina
            
        
