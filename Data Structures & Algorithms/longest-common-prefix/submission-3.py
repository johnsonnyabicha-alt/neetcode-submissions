class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # prefix = strs[0]
        # prefix_len = len(prefix)
        # for s in strs[1:]:
        #     while prefix != s[0: prefix_len]:
        #         prefix_len -= 1
        #         if prefix_len == 0 :
        #             return ""
        #         prefix = prefix[0: prefix_len]
        # return prefix 
        output = []
        for i, string in enumerate(strs[0]):
            for words in strs[1:]:
                if i >= len(words) or words[i] != string:
                    return "".join(output)
            output.append(string)
        return "".join(output)

            
            

