class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [n] * (2*n)
        for i in range(n):
            ans[i] = nums[i]
        for i in range(n):
            ans[i+n] = nums[i]
        return ans
