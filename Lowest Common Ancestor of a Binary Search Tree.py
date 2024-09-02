# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #Time Complexity: O(height of tree) = O(log n)
        #Space Complexity: O(height of tree) = O(log n)
        def dfs(r):
            if r.val == p.val or r.val == q.val or (r.val > p.val and r.val < q.val) or (r.val < p.val and r.val > q.val): 
                return r
            if r.val < p.val and r.val < q.val:
                return dfs(r.right)
            if r.val > p.val and r.val > q.val:
                return dfs(r.left)
        

        return dfs(root)
