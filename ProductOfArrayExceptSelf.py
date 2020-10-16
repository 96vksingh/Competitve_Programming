class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 0
        left = [1 for i in nums]
        output = [1 for i in nums]
        for i in range(1,len(nums)):
            left[i] = left[i-1]* nums[i-1] 
        R = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] = left[i]*R
            R = R*nums[i]
        return output
