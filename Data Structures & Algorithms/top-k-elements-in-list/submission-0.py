class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        output = []
        for a in nums:
            seen[a] += 1
        sorted_items = dict(sorted(seen.items(),key=lambda x:x[1], reverse=True))
        for b in sorted_items.keys():
            output.append(b)
        return output[:k]

        


