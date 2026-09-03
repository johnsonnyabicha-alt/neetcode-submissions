class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for group in strs:
            key = ''.join(sorted(group))
            groups[key].append(group)
        res = [i for i in groups.values()]
        return res

