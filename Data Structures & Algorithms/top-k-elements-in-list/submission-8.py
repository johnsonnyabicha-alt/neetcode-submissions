class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import itertools
        import heapq 
        seen = {}
        for n in nums:
            seen[n] = 1 + seen.get(n,0)
        counter = itertools.count()
        heap_list = [(-value,next(counter),key) for key,value in seen.items()]
        heapq.heapify(heap_list)
        res = []
        while len(res) != k:
            _,_,smallest_val = heapq.heappop(heap_list)
            res.append(smallest_val)
        return res