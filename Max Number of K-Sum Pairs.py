class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        res = 0
        st = set()
        for f in freq:
            if f not in st and (k - f) in freq:
                if f == k - f:
                    res += freq[f] // 2
                else:
                    res += min(freq[f], freq[k-f])
                    st.add(f)
                    st.add(k-f)
        return res
