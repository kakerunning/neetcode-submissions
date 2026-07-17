# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        self.res = 0;

        def depth(node):
            if not node :
                return 0
            else:   
                left = depth(node.left)
                right = depth(node.right)

                self.res = max(self.res, math.fabs(left - right))
                return 1 + max(left, right)
        
        depth(root)
        if self.res > 1:
            return False
        else:
            return True