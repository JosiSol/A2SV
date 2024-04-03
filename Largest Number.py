class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums.sort(key = lambda x: x* 10, reverse = True)
        if nums[0] == str(0):
            return str(0)
        return ''.join(str(num) for num in nums)
