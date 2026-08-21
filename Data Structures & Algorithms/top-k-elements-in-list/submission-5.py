class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        output = []
        for a in nums:
            seen[a] += 1
        vals = tuple(seen.items())
        sorted_items = sorted(vals, key=lambda x:x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]