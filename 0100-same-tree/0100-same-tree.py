# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        list_p = self.traversal(p)
        list_q = self.traversal(q)

        print(list_p)
        print(list_q)

        if len(list_p) != len(list_q):
            return False

        for i in range(len(list_p)):
            if list_p[i] != list_q[i]:
                return False

        return True

    def traversal(self, tree: Optional[TreeNode]) -> list:
        
        if tree == None:
            return [None]

        return [tree.val] + self.traversal(tree.left) + self.traversal(tree.right)