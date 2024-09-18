class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Time Complexity: O(n log n)
        #Space Complexity: O(n)
        time,st = [], []
        for i in range(len(position)):
            count = (target - position[i]) / speed[i]
            time.append(count)
        time = [x for _, x in sorted(zip(position, time))]
        time.reverse()
        
        for timmy in time:
            if not st or (st[-1] < timmy):
                st.append(timmy)

        return len(st)
