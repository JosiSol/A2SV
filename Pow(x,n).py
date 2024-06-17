class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x,n,help):
            if n == 0:
                return help
            elif n < 0:
                return pow(1/x, -n,help)
            if n % 2 == 0:
                return pow(x*x, n // 2, help)
            else:
                return pow(x, n - 1, help * x)
        return pow(x,n,1.0)    
