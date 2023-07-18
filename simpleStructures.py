class StackNode:
    def __init__(self, value, nextNode):
        self.value = value
        self.next = nextNode


class Stack:
    def __init__(self):
        self.top = StackNode(None, None)
        

    def top(self):
        return self.top.next

    def push(self, value):
        newNode = StackNode(value, self.top)
        self.top.next = newNode
        return None
    
    def pop(self):
        self.top.next = self.top.next.next
        return None