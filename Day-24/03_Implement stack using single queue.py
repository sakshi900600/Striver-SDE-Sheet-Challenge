from collections import deque

class Stack:
    def __init__(self):
        self.q = deque()
    
    def push(self, data):
        # Append new element
        self.q.append(data)
        # Rotate the queue so the new element is at the front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    
    def pop(self):
        if self.isEmpty():
            return None
        return self.q.popleft()
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.q[0]
    
    def isEmpty(self):
        return len(self.q) == 0
    
    