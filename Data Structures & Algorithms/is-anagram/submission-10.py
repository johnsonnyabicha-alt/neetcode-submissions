class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_list = list(t)
        counter = 0
        len1, len2 = len(s), len(t)
        for char in s:
            if char in s_list:
                s_list.remove(char)
                counter += 1

        if counter == len1:
            return True 
        else:
            return False
