class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
            Add two numbers represented by two linked lists in reverse order of digits,
            and return the result as a linked list

            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
        """
        sumret = p = ListNode(0)
        accumulator = 0
        while l1 or l2 or accumulator:
            l1,val1 = (l1.next,l1.val) if l1 else (None,0)
            l2,val2 = (l2.next,l2.val) if l2 else (None,0)
            accumulator,val = divmod(val1+val2+accumulator, 10)

            p.next = ListNode(val)
            p = p.next

        return sumret.next


# test 342+465=807
l1=ListNode(2)
l1.next=ListNode(4)
l1.next.next=ListNode(3)
l2=ListNode(5)
l2.next=ListNode(6)
l2.next.next=ListNode(4)

sol = Solution()
ret = p = sol.addTwoNumbers(l1,l2)
retstr =''
while p:
    retstr+=str(p.val)+' -> '
    p=p.next
print(retstr[:-3])
