class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        result = ""

        # Iterate through both strings
        while i < m or j < n:
            if i < m:
                result += word1[i] # Append character from word1
                i += 1
            if j < n:
                result += word2[j] # Append character from word2
                j += 1

        return result

