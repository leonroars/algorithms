class Stack:
    def __init__(self):
        self.stk = []
    
    def push(self, item):
        self.stk.append(item)
    
    def pop(self):
        if not self.isEmpty():
            return self.stk.pop()
        else:
            raise Exception("Stack is empty. pop() can be processed.")
    
    def peek(self):
        if not self.isEmpty():
            return self.stk[-1]
    
    def size(self):
        return len(self.stk)
    
    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False
    def clear(self):
        self.stk = []
        
    def __str__(self):
        return str(self.stk)
