class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = False
        seen = {}
        for i in range(len(nums)):
             value = nums[i]
             if value in seen:
                return True
             seen[value] = True
        return False