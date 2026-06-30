class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # SOLUTION 1:
        # seen = defaultdict(list)
        # for a in strs:
        #     key = "".join(sorted(a))
        #     seen[key].append(a)
        # array = [l for l in seen.values()]
        # return array
        # O(m * nlogn), where m is the number the number of strings
        res = defaultdict(list)
        for a in strs:
            count = [0] * 26
            for char in a:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(a)
        print(res)
        array = [l for l in res.values()]
        return array 




                
        
        
        