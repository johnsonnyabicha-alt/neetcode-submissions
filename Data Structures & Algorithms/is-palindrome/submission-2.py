class Solution:
    def isPalindrome(self, s: str) -> bool:
        # filtered_strs = ''.join(filter(str.isalnum, s.lower()))
        # print(filtered_strs)
        # print(filtered_strs[::-1], "***")
        # if filtered_strs == filtered_strs[::-1]:
        #     return True 
        # else:
        #     return False
        filt_str = ''.join(filter(str.isalnum, s.lower()))
        l = 0
        r = len(filt_str) - 1
        while l < r:
            if filt_str[l] != filt_str[r]:
                return False
            l += 1
            r -= 1
        return True 
             

