
class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def createList(values):
    if not values:
        return None
    
    head = Node(values[0])
    cur = head

    for val in values[1:]:
        cur.next = Node(val)
        cur = cur.next

    return head


def has_cycle(head):
    slow = head
    fast = head.next

    while slow != fast:

        if fast is None or fast.next is None:
            return False

        if fast == slow:
            return True

        fast = fast.next.next
        slow = slow.next

    return True
        


values = [3, 2, 0, -4]
head = createList(values)

head.next.next.next.next = head.next  # values[3] -> values[1]
print(has_cycle(head))
        