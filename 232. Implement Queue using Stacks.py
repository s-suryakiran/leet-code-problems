class MyQueue:
    s1 = []
    s2 = []
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        while (self.s1):
            i = self.s1.pop()
            self.s2.append(i)
        
        x = self.s2.pop()
        while (self.s2):
            i = self.s2.pop()
            self.s1.append(i)
        
        return x

    def peek(self) -> int:
        i = None
        while (self.s1):
            i = self.s1.pop()
            self.s2.append(i)
        x = i
        while (self.s2):
            i = self.s2.pop()
            self.s1.append(i)
        return x
        

    def empty(self) -> bool:
        if (self.s1):
            return False
        else :
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()