class CircularQueue:
    def __init__(self, qsize):
        self.MAX_QSIZE = qsize
        self.cq = [None] * self.MAX_QSIZE
        self.front = 0
        self.rear = 0
    
    def __str__(self):
        return str(self.cq)
    
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1) % self.MAX_QSIZE
            self.cq[self.rear] = item
        else:
            raise Exception("CircularQ is Full!")
        
    def dequeue(self): # Caution. In CQ, 'front' must point the intended empty space's index which was cleared for identifying isFull() / isEmpty() status.
        if not self.isEmpty():
            self.front = (self.front + 1) % self.MAX_QSIZE
            return self.cq[self.front]
        
    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear + 1) % self.MAX_QSIZE
    
    def peek(self):
        return self.cq[self.rear]
    
    def size(self):
        return {self.MAX_QSIZE + (self.rear - self.front)} % self.MAX_QSIZE
    
    def display(self):
        return self.cq
    
    

a = CircularQueue(8)
print(a.isEmpty)
a.enqueue(3)
a.enqueue(4)
a.enqueue(5)
a.dequeue()
print(a.front)
print(a.rear)
print(a.cq)
print(a.size)
print(a.isEmpty)
print(a.isFull)