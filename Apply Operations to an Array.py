class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = 2 * nums[i]
                nums[i+1] = 0
        a = []
        for i in nums:
            if i != 0:
                a.append(i)
        for i in nums:
            if i == 0:
                a.append(i)
        return a

