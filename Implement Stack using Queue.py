class MyStack:

    #Space Complexity: O(n)
    def __init__(self): #Time Complexity: O(1)
        self.q1 = deque()
        self.q2 = deque()
        self.cur_size = 0


    def push(self, x: int) -> None: #Time Complexity: O(1)
        self.q1.append(x)
        self.cur_size += 1


    def pop(self) -> int: #Time Complexity: O(n)
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        self.q1,self.q2 = self.q2,self.q1
        self.cur_size -= 1
        return self.q2.popleft()


    def top(self) -> int: #Time Complexity: O(1)
        return self.q1[self.cur_size - 1] if not self.empty() else -1

    def empty(self) -> bool: #Time Complexity: O(1)
        if self.q1:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
