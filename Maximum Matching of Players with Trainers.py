class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        count = 0

        for t in trainers:
            while len(players) > 0 and players[0] > t:
                players.pop(0)
            if len(players) > 0 and players[0] <= t:
                count += 1
                players.pop(0)
        return count
