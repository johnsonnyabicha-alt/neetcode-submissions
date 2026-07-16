class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = []
        for i, char in enumerate(strs[0]): # go through each index & letter
            for words in strs[1:]:# look at every other string
                if i >= len(words) or words[i] != char: 
                    return "".join(output)
            output.append(char)
        return "".join(output)

            
            

