class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
            Add two numbers represented by two linked lists in forward order of digits,
            and return the result as a linked list in forward order.
            Cannot reverse the input lists

            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
        """
        ret=p=ListNode(0)
        s1,s2=[],[]
        accum=0
        while l1:
            s1.append(l1.val)
            l1=l1.next
        while l2:
            s2.append(l2.val)
            l2=l2.next
        while s1 or s2 or accum:
            n1 = s1.pop() if s1 else 0
            n2 = s2.pop() if s2 else 0
            accum,n = divmod(n1+n2+accum,10)
            p.val = n
            q=p
            p=ListNode(0)
            p.next=q
        return p.next


# test 342+465=807
l1=ListNode(3)
l1.next=ListNode(4)
l1.next.next=ListNode(2)
l2=ListNode(4)
l2.next=ListNode(6)
l2.next.next=ListNode(5)

sol = Solution()
ret = p = sol.addTwoNumbers(l1,l2)
retstr =''
while p:
    retstr+=str(p.val)+' -> '
    p=p.next
print(retstr[:-3])