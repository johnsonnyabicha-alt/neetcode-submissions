class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src,targ,w in times:
            adj[src].append([w,targ])
        min_heap = [[0,k]]
        shortest_path = {}
        while min_heap:
            w1,n1 = heapq.heappop(min_heap)
            if n1 in shortest_path:
                continue 
            shortest_path[n1] = w1
            for w2,n2 in adj[n1]:
                heapq.heappush(min_heap,[w1+w2,n2])
        if len(shortest_path) != n:
            return int(-1)
        else:
            return max(shortest_path.values())
         
            

        
         
