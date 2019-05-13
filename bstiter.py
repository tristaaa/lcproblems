# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# iterator over a binary search tree (BST)
class BSTIterator:

    def __init__(self, root):
        self.stack=[]
        curr = root
        # once you get to a TreeNode, in order to get the smallest, 
        # you need to go all the way down its left branch. 
        # So our first step is to point to the left most TreeNode
        while curr:
            self.stack.append(curr)
            curr=curr.left
        

    def next(self):
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        # When the current TreeNode has a right branch 
        # (It cannot have left branch, remember we traversal to the left most),
        # we need to jump to its right child first and then
        # traversal to its right child's left most TreeNode
        curr = node.right
        while curr:
            self.stack.append(curr)
            curr = curr.left
        return node.val
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        """
        return len(self.stack)>0


# test
# root = TreeNode(5)
# root.left = TreeNode(3)
# root.left.left = TreeNode(2)
# root.left.right = TreeNode(4)
# root.right = TreeNode(6)
# root.right.right = TreeNode(7)
# obj = BSTIterator(root)
# while obj.hasNext():
#     print(obj.next())