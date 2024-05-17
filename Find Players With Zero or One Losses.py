class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss = Counter()
        for winner, loser in matches:
            loss[loser] += 1
            loss[winner] += 0
        ans = [ [],[] ]
        for player in sorted(loss.keys()):
            if loss[player] == 0:
                ans[0].append(player)
            elif loss[player] == 1:
                ans[1].append(player)
        return ans
