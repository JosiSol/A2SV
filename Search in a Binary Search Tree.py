# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #Time Complexity: O(height of tree) = O(log n)
        #Space Complexity: O(height of tree) = O(log n)
        def dfs(r):
            if not r:
                return r
            if r.val == val:
                return r
            if r.val > val:
                return dfs(r.left)
            if r.val < val:
                return dfs(r.right)
        

        return dfs(root)
