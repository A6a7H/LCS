'''
Given a linked list, write a function to reverse every k nodes (where k is an input to the function).
Example:
Inputs: 1->2->3->4->5->6->7->8->NULL and k = 3
Output: 3->2->1->6->5->4->8->7->NULL.
Inputs: 1->2->3->4->5->6->7->8->NULL and k = 5
Output: 5->4->3->2->1->8->7->6->NULL.
'''

def reverse(lst, k):
    head = lst
    i = 1
    while lst:
        if i % k == 0:
            next_node = lst.next
            
