class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        miss_n = len(nums)

        for i in range(len(nums)):
            if i != nums[i]:
                miss_n = i
                return miss_n
        
        return miss_n