# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        preorder: (Root, Left, Right) using dfs, using stack
        the root.val can be None

        return the preorder traversal list of a binary tree
        :type root: : TreeNode
        :rtype: List[int]
        """
        # recursive
        # ret = []
        # def dfs(root):
        #     if root:
        #         if root.val:
        #             ret.append(root.val)
        #         dfs(root.left)
        #         dfs(root.right)
        # dfs(root)
        # return ret

        # iterative
        # basecase
        if not root:
            return []
        stack = [root]
        ret=[]
        while stack:
            node = stack.pop()
            ret.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return ret


sol = Solution()
#      1
#     / \
#    2   6
#  /  \
# 4    5
lines=["     1","    / \\","   2   6"," /  \\","4    5"]
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(6)
print("Given the binary tree:\n","\n".join(lines))
print("the preorder of the binary tree is: %s" %(sol.preorderTraversal(root)))



