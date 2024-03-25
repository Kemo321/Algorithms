"""The digits are stored in reverse order, and each of their nodes
 contains a single digit. Add the two numbers and return the sum as 
 a linked list."""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
    dummyHead=ListNode(0)
    tail=dummyHead

    Sum=0
    power=0

    helper = []
    value = 0
    carry = 0

    while l1 or l2:
        value += carry
        carry = 0
        if l1:
            value += l1.val
            l1 = l1.next
        if l2:
            value += l2.val
            l2 = l2.next
        carry = value / 10
        value = value % 10
        helper.append(value)
        value = 0
    
    if int(carry) != 0:
        helper.append(carry)

    for i in range(len(helper)):
        new_node=ListNode(int(helper[i]))
        tail.next=new_node
        tail=tail.next
    
    return dummyHead.next
