class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
    
        # Step 1: Calculate prefix products (left side)
        # output[i] will store the product of all numbers to the left of index i
        prefix_product = 1
        for i in range(n):
            output[i] = prefix_product
            prefix_product *= nums[i]
        
    # Step 2: Calculate suffix products (right side) on the fly
    # Multiply the existing prefix product with the suffix product
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix_product
            suffix_product *= nums[i]
        
        return output