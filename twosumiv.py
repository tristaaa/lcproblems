class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)

class Solution:
    def findTarget(self, root, k):
        # using bfs 
        # if root==None:
        #     return False
        # queue=[root]
        # visited = set()
        # while queue:
        #     i = queue.pop(0)
        #     if k-i.val in visited:
        #         return True
        #     visited.add(i.val)
        #     if i.left:
        #         queue.append(i.left)
        #     if i.right:
        #         queue.append(i.right)
        # return False

        # using dfs recursive version
        # visited = set()
        # def dfs(root):
        #     if not root: return False
        #     # print(root.val,visited)
        #     if k-root.val in visited: return True
        #     visited.add(root.val)
        #     return dfs(root.left) or dfs(root.right)
        # return dfs(root)

        # using dfs stack version
        visited = set()
        stack = [root]
        while stack:
            root = stack.pop()
            if not root: return False
            if k-root.val in visited: return True
            visited.add(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return False

        # using two stacks version, don't have to iterate over whole BST
        # stackL,stackR=[],[] # respectively get the next smallest, largest value
        # curr = root
        # while curr:
        #     stackL.append(curr)
        #     curr=curr.left
        # curr = root
        # while curr:
        #     stackR.append(curr)
        #     curr=curr.right

        # while stackL[-1].val!=stackR[-1].val:
        #     p,q=stackL[-1].val,stackR[-1].val
        #     # print(p,q)
        #     if p+q == k:
        #         return True
        #     elif p+q<k:
        #         curr = stackL.pop().right
        #         while curr:
        #             stackL.append(curr)
        #             curr=curr.left
        #     else:
        #         curr = stackR.pop().left
        #         while curr:
        #             stackR.append(curr)
        #             curr=curr.right
        # return False



# test
sol=Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(7)
target=5

print(sol.findTarget(root,target))