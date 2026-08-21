class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for x in nums:
            hashmap[x] = 1 + hashmap.get(x, 0)
        counts = [[]for i in range(len(nums)+1)]
        for n, c in hashmap.items():
            counts[c].append(n)
        res = []
        for i in range(len(counts)-1, 0, -1):
            for n in counts[i]:
                res.append(n)
                if len(res) == k:
                    return res
        

        
        
        
        
        
