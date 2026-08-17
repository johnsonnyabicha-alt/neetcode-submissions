class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a, int1 in enumerate(nums):
            unknown = target - int1
            for b, int2 in enumerate(nums[a+1:]):
                if int2 == unknown:
                    return[a,a+1+b]
            