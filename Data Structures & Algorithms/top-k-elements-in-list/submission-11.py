class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        if len(nums) <= 1:
            return nums
        for i in nums:
            seen[i]+= 1
        freq = [[] for i in range(len(nums)+1)]
        for n,c in seen.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            if freq[i]:
                res.extend(freq[i]) 
            if len(res) == k:
                return res

