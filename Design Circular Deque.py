class MyCircularDeque:
    #Time Complexity: O(1) for all functions
    #Space Complexity: O(k)
    def __init__(self, k: int):
        self.cur_sz = 0
        self.l = 0
        self.r = 0
        self.mx_sz = k
        self.st = [0] * k

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.cur_sz += 1
            self.st[self.r] = value
            self.r += 1
            if self.r == self.mx_sz:
                self.r = 0
            
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.cur_sz += 1
            self.l -= 1
            if self.l < 0:
                self.l = self.mx_sz - 1
            self.st[self.l] = value
            return True
        return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.cur_sz -= 1
            self.r -= 1
            if self.r < 0:
                self.r = self.mx_sz - 1
            return True
        return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.cur_sz -= 1
            self.l += 1
            if self.l == self.mx_sz:
                self.l = 0
            return True
        return False

    def getFront(self) -> int:
        return self.st[self.r - 1] if not self.isEmpty() else - 1

    def getRear(self) -> int:
        return self.st[self.l] if not self.isEmpty() else - 1

    def isEmpty(self) -> bool:
        return not self.cur_sz

    def isFull(self) -> bool:
        return self.cur_sz == self.mx_sz
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
