"""Перевернуть список"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
 
    def create_list(self, values):
        if not values:
            return None
        
        self.head = Node(values[0])
        cur = self.head

        for val in values[1:]:
            cur.next = Node(val)
            cur = cur.next

        return self.head
    
    def print_list(self):
        cur = self.head
        while cur:
            print(str(cur.val) + " -> ", end="")
            cur = cur.next

        print("None")
    
    def reverse_list(self):
        if self.head is None:
            return None
        
        prev = None
        cur = head
        
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        self.head = prev     # Если возьмем head = cur, то head будет None, prev - ранее последний узел, сейчас - начало перевернутого списка
        return self.head


values = [1, 2, 3, 4, 5]

linked_list = LinkedList()

head = linked_list.create_list(values)
linked_list.print_list()

reversed_head = linked_list.reverse_list()  
linked_list.print_list()