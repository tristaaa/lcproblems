# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # 1. recurisve version, preorder traversal(DLR), '1,2,#,#,3,4,#,#,5,#,#'
        # if not root: return '#'            
        # serialret = [str(root.val)]
        # serialret.append(self.serialize(root.left))
        # serialret.append(self.serialize(root.right))
        # return ','.join(serialret)

        # 2. neat recursive version
        # return root and ','.join((str(root.val), self.serialize(root.left), self.serialize(root.right))) or '#'

        # 3. iterative DFS, '1,2,#,#,3,4,#,#,5,#'
        if not root: return '#'

        ret = []
        stack = []
        cur = root
        while cur or stack:
            if cur:
                ret.append(str(cur.val))
                stack.append(cur)
                cur = cur.left
            else:
                ret.append('#')
                cur = stack.pop()
                cur = cur.right

        return ','.join(ret)



    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def des():
            val = vals.__next__()
            if val =='#': return None
            root = TreeNode(int(val))
            root.left = des()
            root.right = des()
            return root

        vals = iter(data.split(','))
        return des()


from bstiter import BSTIterator

# test binary tree
#   1
#  / \
# 2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
print("the test binary tree shown in inorder traversal: ")
obj = BSTIterator(root)
while obj.hasNext():
    print(obj.next())
print()

# Your Codec object will be instantiated and called as such:
codec = Codec()
serialret = codec.serialize(root)
print("the serialized string of the original binary tree is(preorder traversal): ", serialret)

deserialret = codec.deserialize(codec.serialize(root))
print("\nthe deserialized tree shown in inorder traversal: ")
obj = BSTIterator(deserialret)
while obj.hasNext():
    print(obj.next())