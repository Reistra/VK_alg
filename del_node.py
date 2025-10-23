"""Удалить элемент из односвязного списка по значению. """


class Node:
    def __init__(self, val=None, next=None):
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
    
    def remove_element(self, val):
        dummy = Node(next=self.head)
        prev = dummy
        cur = self.head

        while cur:
            if cur.val == val:
                prev.next = cur.next
                break

            prev = cur
            cur = cur.next

        self.head = dummy.next
        return self.head
    
    def print_list(self):
        cur = self.head
        while cur:
            print(str(cur.val) + " -> ", end="")
            cur = cur.next

        print("None")
    

linked_list = LinkedList()

linked_list.create_list([1,2,3,4,5,6,7,8,9,0])

linked_list.print_list()

linked_list.remove_element(5)
linked_list.print_list()

linked_list.remove_element(1)
linked_list.print_list()

linked_list.remove_element(0)
linked_list.print_list()