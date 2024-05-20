class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, mc = 0, 0
        for r, num in enumerate(nums):
            k -= 1 - num
            if k < 0:
                k += 1 - nums[l]
                l += 1
            else:
                mc = max(mc, r - l + 1)
        return mc
