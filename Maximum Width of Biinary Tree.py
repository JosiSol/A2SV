# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        if not root:
            return 0
        q = deque([(root, 0)])
        mx = 1
        while q:
            n = len(q)
            _, first = q[0]
            _, last = q[-1]
            mx = max(mx, last - first + 1)
            for _ in range(n):
                node, pos = q.popleft()
                if node.left:
                    q.append((node.left, 2 * pos))
                if node.right:
                    q.append((node.right, 2 * pos + 1))
                mx = max(mx, n)
        return mx
