class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        r,count = 0,0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    count += 1
                else:
                    continue
            result.append(count)
            count = 0
    
        return result
            
