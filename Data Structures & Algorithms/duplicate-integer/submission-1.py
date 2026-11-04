class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenElements = {}

        for number in nums:
            if number in seenElements:
                return True
            seenElements[number] = True

        return False
        