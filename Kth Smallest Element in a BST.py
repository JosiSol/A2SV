# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        def dfs(r):
            if not r:
                return []
            else:
                return dfs(r.left) + [r.val] + dfs(r.right)


        res = dfs(root)
        return res[k-1]
