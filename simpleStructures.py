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
    def __init__(self, value, prev):
        self.value = value
        self.prev = prev

class Queue:
    def __init__(self):
        self.front = QueueNode(None, None)
        self.back = QueueNode(None, None)
    
    def top(self):
        return QueueNode(self.front.prev.value, self.front.prev)

    def push(self, value):
        newNode = QueueNode(value, self.back.prev)
        # self.back.prev = QueueNode(value, newNode)
        self.back = QueueNode(None, newNode)

    def pop(self):
        self.front.prev.prev = QueueNode(self.front.prev.prev, self.front)
        return None

a = Queue()
a.push(1)
print(a.top().value)
# a.push(2)
# a.pop()
# print(a.top().value)
