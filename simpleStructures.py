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
    def __init__(self, value, node):
        self.value = value
        self.node = node

# class Queue:
#     def __init__(self):
#         self.front = QueueNode(None, None)
#         self.back = QueueNode(None, self.front)
        
#     def top(self):
#         return QueueNode(self.front.node.value, self.front.node) #if self.front.node != None else QueueNode(None, )

#     def push(self, value):
#         newNode = QueueNode(value, self.back)
#         if self.back.node.node: self.back.node = QueueNode(self.back.node.value, newNode)
#         else: self.front = QueueNode(self.back.node.value, newNode)
#         self.back = QueueNode(None, newNode)
        
#     def pop(self):
#         self.front = QueueNode(self.front.node.node.value, self.front.node.node)
#         return None

class Queue:
    def __init__(self):
        self.back = QueueNode(None, None)
        self.front = QueueNode(None, self.back)
        
    def top(self):
        return QueueNode(self.front.node.value, self.front.node) #if self.front.node != None else QueueNode(None, )

    def push(self, value):
        newNode = QueueNode(value, self.back.node)
        # if self.back.node.node: self.back.node = QueueNode(self.back.node.value, newNode)
        # else: self.front = QueueNode(self.back.node.value, newNode)
        self.back = QueueNode(None, newNode)
        
    def pop(self):
        self.front = QueueNode(self.front.node.node.value, self.front.node.node)
        return None

a = Queue()
a.push(1)
a.push(2)
# print(a.top().value)
print(a.front.node.value)
print(a.back.node.value)
a.pop()
a.push(3)
print(a.front.node.value)
print(a.back.node.value)
# print(a.top().value)
