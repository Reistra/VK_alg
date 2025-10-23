"""принимает на вход два отсортированных односвязных списка и объединяет их в один отсортированный список. """

class Node:
    def __init__(self, val=0, next=None):
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


def merge_sorted_lists(l1, l2):
    dummy = Node()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return dummy.next


list1 = LinkedList()
list1.create_list([1, 3, 5, 7])

list2 = LinkedList()
list2.create_list([2, 4, 6, 8])

merged_head = LinkedList()
merged_head = merge_sorted_lists(list1.head, list2.head)

cur = merged_head
while cur:
    print(f"{cur.val} -> ", end="")
    cur = cur.next
print("None")