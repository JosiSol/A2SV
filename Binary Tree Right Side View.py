# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        if not root:
            return []
        def dfs(node, depth):
            if not node:
                return
            if depth == len(right_view):
                right_view.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        right_view = []
        dfs(root, 0)
        return right_view
