class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        seen = defaultdict(int)
        seen2 = defaultdict(int)
        for i in s:
            seen[i] += 1
        for i in t:
            seen2[i] += 1
        for c in seen:
            if seen[c] != seen2[c]:
                return False
        return True