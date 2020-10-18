"""
21. Merge Two Sorted Lists
Easy

5147

646

Add to List

Share
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

 

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.

"""

# solution 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # create dummy and output linked list
        dummy_var = final_tree = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                # set node to final tree
                final_tree.next = l1
                # shift the node to next 
                l1 = l1.next
            else:
                # set node to final tree
                final_tree.next = l2
                # shift the node to next 
                l2 = l2.next
            # set the next node
            final_tree = final_tree.next
        # if one one linked list is ended add the another linked list to the final_tree
        final_tree.next = l1 or l2
        return dummy_var.next