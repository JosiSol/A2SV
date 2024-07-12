class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        #Space Complexity: O(1)
        #TIme Complexity: O(n)
        res = 0
        for i, j in exnumerate(tickets):
            if i <= k:
                res += min(j, tickets[k])
            else:
                res += min(j, tickets[k] - 1)
        return res
