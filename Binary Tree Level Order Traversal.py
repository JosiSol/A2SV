# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        queue = deque()
        res = []
        if not root:
            return []
        queue.append(root)
        while queue:
            n = len(queue)
            lvl = []
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                lvl.append(node.val)
            res.append(lvl)
        return res
            
        
        
