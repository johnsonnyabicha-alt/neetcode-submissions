class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        empty = []
        for a in range(len(nums)):
            for b in range(a+1, len(nums)):
                if nums[a] + nums[b] == target:
                    empty.insert(0, a)
                    empty.insert(1, b)
        return empty
        

        