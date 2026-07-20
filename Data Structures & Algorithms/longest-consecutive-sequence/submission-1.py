class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # the beginning of a sequence start when a number i-1 is not in the set
        nums_set = set(nums)
        longest = 0
        for ints in nums_set:
            if (ints - 1) not in nums_set:
                length = 1 
                while (ints + length) in nums_set:
                    length += 1
                longest = max(longest, length)

        return longest

                
