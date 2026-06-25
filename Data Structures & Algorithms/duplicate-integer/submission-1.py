class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = []
        counter = 0
        for i in nums:
            if i in dups:
                counter += 1
            else:
                dups.append(i)
        if counter > 0:
            return True 
        else:
            return False
        # USING SETS 
        # numset = set(nums)
        # if len(nums) != len(numset):
        #     return True
        # else:
        #     return False


