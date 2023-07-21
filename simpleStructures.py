# STACK 
class StackNode:
    def __init__(self, value, nextNode):
        self.value = value
        self.next = nextNode

class Stack:
    def __init__(self):
        self.head = StackNode(None, None)
        

    def top(self):
        return StackNode(self.head.next.value, self.head.next) if self.head.next != None else None
        # return self.head.next if self.head.next != None else None

    def push(self, value):
        newNode = StackNode(value, self.head.next)
        self.head = StackNode(value, newNode) # value -> None
        return None
    
    def pop(self):
        self.head = StackNode(self.head.next.next.value, self.head.next.next) #1st arg -> None
        return None


# QUEUE
class QueueNode:
    def __init__(self, value):
        self.value = value
        self.node = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        
    def top(self):
        return self.front.value #if self.front.node != None else QueueNode(None, )

    def push(self, value):
        newNode = QueueNode(value)
        if not self.back: self.front = newNode
        else: self.back.node = newNode
        self.back = newNode
        
    def pop(self):
        if self.front != self.back:
            res = self.front
            self.front = self.front.node
            return res
        res = self.front
        self.front = None
        self.back = None
        return res

