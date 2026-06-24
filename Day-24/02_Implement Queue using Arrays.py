
# Implement simple queue using array

class simple_q():
    def __init__(self, cap):
        self.cap = cap
        self.front = -1
        self.rear = -1
        self.container = [0]*cap
    

    def push(self, data):
        # overflow
        if self.rear >= self.cap-1:
            return None
        
        if self.front == self.rear == -1:
            self.front = 0
            self.rear = 0

            self.container[self.rear] = data
        
        else:
            self.rear += 1
            self.container[self.rear] = data
    

    def pop(self):
        if self.front == -1 or self.front > self.rear:
            return None

        if self.front > self.rear:
            self.front = -1
            self.rear = -1
        
        data = self.container[self.front]
        self.front += 1
        return data
    

    def peek(self):
        if self.front == -1 or self.front > self.rear:
            return None
        
        return self.container[self.front]
    

    def isEmpty(self):
        return self.front == -1 or self.front > self.rear
    

    def size(self):
        if self.isEmpty():
            return 0

        return self.rear - self.front + 1


def Q1():

    q = simple_q(5)
    q.push(1)
    q.push(2)
    q.push(3)
    # q.push(4)
    # q.push(5)
    # print(q.push(6))

    # q.pop()
    # q.pop()
    # q.pop()
    # print(q.pop())
    # print(q.peek())
    # print(q.isEmpty())
    print(q.size())


    while not q.isEmpty():
        print(q.peek(), end=" ")
        q.pop()
