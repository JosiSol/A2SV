class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr), 1, -1):
            x = arr.index(i)
            result.extend([x + 1, i])
            arr = arr[:x:-1] + arr[:x]
        return result
