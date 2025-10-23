"""Является ли str1 подпоследовательностью str2? Решить с помозью очередей"""

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Queque:
    def __init__(self):
        self.first = None
        self.last = None

    def push(self, val):
        val = Node(val)

        if not self.first:
            self.first = self.last = val
        else:
            self.last.next = val
            self.last = val

    def pop(self):
        if not self.first:
            return None
        
        val = self.first.val
        self.first = self.first.next

        if not self.first:
            self.last = None

        return val
    
    def print_queue(self):
        cur = self.first
        while cur:
            print(f"{cur.val} <- ", end="")
            cur = cur.next
        print("None")


def is_subsequence(str1, str2):
    q = Queque()
    for chr1 in str1:
        q.push(chr1)

    for chr2 in str2:
        if q.first and q.first.val == chr2:
            q.pop()
        
    return q.first is None


str1 = "abc2"
str2 = "ahbgdc"

print(is_subsequence(str1, str2))  # True