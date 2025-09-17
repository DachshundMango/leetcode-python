# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        result = ListNode()
        pointer = result

        while (True):

            if (list1 == None) and (list2 == None):
                return None 

            elif (list1 == None) and (list2 != None):
                while list2 != None:
                    pointer.val = list2.val
                    list2 = list2.next
                    if list2 == None:
                        break
                    pointer.next = ListNode()
                    pointer = pointer.next
                    continue
                return result

            elif (list2 == None) and (list1 != None):
                while list1 != None:
                    pointer.val = list1.val
                    list1 = list1.next
                    if list1 == None:
                        break
                    pointer.next = ListNode()
                    pointer = pointer.next
                    continue                    
                return result

            else:
                if list2.val <= list1.val:
                    pointer.val = list2.val
                    list2 = list2.next
                else:
                    pointer.val = list1.val
                    list1 = list1.next

                pointer.next = ListNode()
                pointer = pointer.next
                continue

            return result
