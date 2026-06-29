class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # s_list = list(t)
        # counter = 0
        # len1, len2 = len(s), len(t)
        # for char in s:
        #     if char in s_list:
        #         s_list.remove(char)
        #         counter += 1

        # if counter == len1:
        #     return True 
        # else:
        #     return False


        if len(s) != len(t):
            return False
        s_list= defaultdict(int)
        b_list = defaultdict(int)
        for a in s:
            s_list[a] += 1
        for b in t:
            b_list[b] += 1
        if sorted(s_list.items()) == sorted(b_list.items()):
            return True 
        else:
            return False
        

        
