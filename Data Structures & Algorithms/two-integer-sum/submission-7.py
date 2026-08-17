class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashMap = {}
        for a in range(len(nums)):
            unknown = target - nums[a]
            if unknown in HashMap:
                return [HashMap[unknown], a]
            HashMap[nums[a]] = a
            