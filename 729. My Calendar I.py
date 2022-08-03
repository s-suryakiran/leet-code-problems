class MyCalendar:
    def __init__(self):
        self.range = []
        

    def book(self, start: int, end: int) -> bool:
        if self.range == []:
            self.range.append([start, end])
            return True
        
        for i in self.range:
            if start < i[1] and end > i[0]:
                return False

        self.range.append([start, end])
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)