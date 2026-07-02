class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_strs = ''.join(filter(str.isalnum, s.lower()))
        print(filtered_strs)
        print(filtered_strs[::-1], "***")
        if filtered_strs == filtered_strs[::-1]:
            return True 
        else:
            return False