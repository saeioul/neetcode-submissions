class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Gather our allies.
        n = len(nums)
        prefProduct = [0] * n
        suffProduct = [0] * n
        resProduct  = [0] * n

        # edge cases to be handled: there is nothing left/right our prefix arays.
        prefProduct[0] = 1
        suffProduct[n - 1] = 1

        for i in range(1, n):
            prefProduct[i] = nums[i - 1] * prefProduct[i - 1]

        # this looks weird because we want the iterator to stop at 0. 
        # range will exclude the end argument in math it would be [n-2, -1)
        for i in range(n - 2, -1, -1):
            suffProduct[i] = nums[i + 1] * suffProduct[i + 1]

        for i in range(0, n):
            resProduct[i] = prefProduct[i] * suffProduct[i]

        return resProduct