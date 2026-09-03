class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        for n in nums:
            seen[n] += 1
        ordered = sorted(seen, key = lambda x:seen[x], reverse= True)
        return ordered[:k]