class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0
        for num in numbers:
            if num - 1 not in numbers:
                current_number = num
                length = 1
                while current_number + 1 in numbers:
                    current_number += 1
                    length += 1
                longest = max(longest, length)
        return longest