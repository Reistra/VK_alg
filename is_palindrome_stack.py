"""Является ли слово палиндромом? Решить с помощью стека."""


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
    
class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        
        val = self.top.val
        self.top = self.top.next
        return val
    

    def is_palindrome(self, word):
        for char in word:
            self.push(char)
        
        for char in word:
            if char != self.pop():
                return False
        
        return True


values = [1, 2, 3, 2, 1]

stack = Stack()
print(stack.is_palindrome("racecar"))  # True
print(stack.is_palindrome("hello"))    # False
print(stack.is_palindrome(values))     # True