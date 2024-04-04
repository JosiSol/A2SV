class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(c**0.5) + 1):
            x = c - a ** 2
            b = int(x ** 0.5)
            if x == b ** 2:
                return True
        return False
