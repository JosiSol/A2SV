class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        res,bob,alice = 0,0,n-2
        while bob < alice:
            res += piles[alice]
            alice -= 2
            bob += 1
        return res
