class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for a in strs:
            key = "".join(sorted(a))
            seen[key].append(a)
        array = [l for l in seen.values()]
        return array

                
        
        
        