class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        max_sum = sum(nums[:k])
        current = max_sum

        for r in range(k, len(nums)):
            current += nums[r]
            current -= nums[l]
            l += 1

            max_sum = max(max_sum, current)
        
        return max_sum / k
