"""Выдать центральное значение связного списка"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return
        
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def list_center(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.val 
    
    def print_list(self):
        cur = self.head
        while cur:
            print(str(cur.val) + " -> ", end="")
            cur = cur.next

        print("None")


linked_list = LinkedList()
for num in range(1,8):
    linked_list.append(num)

linked_list.print_list()
print(linked_list.list_center())