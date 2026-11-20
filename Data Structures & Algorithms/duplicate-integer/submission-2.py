class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        easyMap = {}

        for item in nums:
            if item in easyMap:
                return True

            easyMap[item] = True
        
        return False