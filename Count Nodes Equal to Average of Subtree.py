# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        #Time Complexity: O(n)
        #Space Complexity: O(height of tree)
        def dfs(r):
            if not r:
                return (0,0,0)
            left_sum, left_count, left_matches = dfs(r.left)
            right_sum, right_count, right_matches = dfs(r.right)

            total_sum = left_sum + right_sum + r.val
            total_count = left_count + right_count + 1

            average = total_sum // total_count
            match = 1 if r.val == average else 0

            return (total_sum, total_count, left_matches + right_matches + match)
        
        
        _,_,total_matches = dfs(root)
        return total_mat
