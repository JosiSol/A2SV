class DataStream:

    #Time Complexity: O(1) 
    #Space Complexity: O(k)
    def __init__(self, value: int, k: int):
        self.q = deque()
        self.value = value
        self.k = k
        self.size = 0
        self.b = 0


    def consec(self, num: int) -> bool:
        if self.size >= self.k:
            a = self.q.popleft()
            if a == self.value:
                self.b -= 1
        self.q.append(num)
        self.size += 1
        if num == self.value:
            self.b += 1
        return self.b == self.k
        
                
# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
