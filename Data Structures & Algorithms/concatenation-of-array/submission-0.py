class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # we concatenate arrays with '+'
        ans = []
        for i in nums:
            ans.append(i)
        return ans + ans 