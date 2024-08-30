# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        #Time Complexity: O(nodes(n1) + nodes(n2)) = O(n + m)
        #Space Complexity: O(nodes(n1) + nodes(n2)) = O(n + m)
        if not root1 and not root2:
            return None
        tree = TreeNode()    
        
        def dfs(n1,n2, mv):
            if (n1 and n1.left) or (n2 and n2.left):
                mv.left = TreeNode()
            if (n1 and n1.right) or (n2 and n2.right):
                mv.right = TreeNode()
            if n1 and n2:
                mv.val = n1.val + n2.val
                dfs(n1.left, n2.left, mv.left)
                dfs(n1.right, n2.right, mv.right)
            elif n1:
                mv.val = n1.val
                dfs(n1.left, n2, mv.left)
                dfs(n1.right, n2, mv.right)
            elif n2:
                mv.val = n2.val
                dfs(n1, n2.left, mv.left)
                dfs(n1, n2.right, mv.right)
            return


        dfs(root1, root2, tree)
        return tree

