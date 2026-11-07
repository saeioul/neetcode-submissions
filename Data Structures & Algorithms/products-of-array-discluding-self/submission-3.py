class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # The key for O(n) is to avoid recomputation of products.

        n = len(nums)

        # Prefix: all products before i
        pref = [0] * n
        suf  = [0] * n
        res  = [0] * n

        # Preserve the product identity.
        pref[0] = 1
        suf[n -1] = 1

        # Compute product prefixes 
        for i in range(1, n):
            pref[i] = pref[i - 1] * nums[i - 1]

        # Compute product suffixes
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]

        # Compute responses. This works because
        # pref/suf hold values for values prev/after to i.
        for i in range(0,n):
            res[i] = suf[i] * pref[i]

        return res