class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max(nums)
        i = nums.index(max1)
        del nums[i] 
        max2 = max(nums)
        return (max1-1) *(max2 - 1)