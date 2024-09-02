# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #Time Complexity: O(n)
        #Space Complexity: O(height of tree)
        def dfs(r, low, high):
            if not r:
                return True
            if not (low < r.val < high):
                return False
            return dfs(r.left, low, r.val) and dfs(r.right, r.val, high)
        

        return dfs(root, float('-inf'), float('inf'))
