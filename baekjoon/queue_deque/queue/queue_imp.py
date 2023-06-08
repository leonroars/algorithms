class Queue:
    def __init__(self):
        self.q = []
    
    def __str__(self):
        return str(self.q)
    
    def enqueue(self, item):
        self.q.append(item)
        
    def dequeue(self):
        if not self.isEmpty():
            return self.q.pop()
        
    def isEmpty(self):
        if len(self.q) == 0:
            return True
        else:
            return False
    
    def size(self):
        return len(self.q)
    
    def peek(self):
        if not self.isEmpty():
            return self.q[-1]
