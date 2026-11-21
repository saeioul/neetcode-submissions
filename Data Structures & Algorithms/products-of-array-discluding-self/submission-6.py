class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        To solve this in o(n) we need to leverage the prefix/postfix product property
        '''

        # Representation first: prefix and postfix product array holders
        # prefix:  [ 1, 0, 0 , ...]
        # postfix: [ 0, ...  ,  1 ]

        n = len(nums)

        pref = [0] * n
        post = [0] * n
        prod = [0] * n

        # Never forget to preserve product identity
        pref[0]  = 1
        post[-1] = 1

        # First pass is computing prefixes: start left to right
        # prefix:  [ 1, 0, 0 , ...]
        # nums:    [ a, b, c , n]
        for i in range(1, n):
            pref[i] = pref[i - 1] * nums[i - 1]

        # Second pass is computing postfixes: start right to left
        # postfix:  [ 1, 0, 0 , ...]
        # nums:     [ a, b, c , n] 
        for i in range(n - 2, -1, -1):
            post[i] = post[i + 1] * nums[i + 1]

        # Final pass builds the complete product
        for i in range(0, n):
            prod[i] = pref[i] * post[i]
        
        return prod


