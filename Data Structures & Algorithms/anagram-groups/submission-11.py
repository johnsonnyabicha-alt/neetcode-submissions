class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        HashMap = defaultdict(list)
        for strings in strs:
            characters = [0] * 26
            for char in strings:
                characters[ord(char) - ord('a')] += 1
            HashMap[tuple(characters)].append(strings)
        return list(HashMap.values())
                