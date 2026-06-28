class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums)//2
        result = -1
        if target >= nums[mid]:
            for i in range(mid, len(nums)):
                if nums[i] == target:
                    result = i
        else:
            for i in range(0, mid):
                if nums[i] == target:
                    result = i
        return result