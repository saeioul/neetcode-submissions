class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Key to this problem is using pre/post computed products
        relative to the requested index.
        '''
        inputLen = len(nums)
        preProd = [0] * inputLen
        posProd = [0] * inputLen

        # We need this to preserve the product identity when
        # computing first products
        preProd[0] = 1
        posProd[inputLen - 1] = 1

        # Compute prefix array
        # [1, 0, ..., 0 ]
        for i in range(1, inputLen):
            preProd[i] = preProd[i - 1] * nums[i - 1]

        # Compute postfix array
        # [ 0, 0, ... , 1 ]
        for i in range(inputLen - 2, -1, -1):
            posProd[i] = posProd[i + 1] * nums[i + 1]


        # Compute all products but i
        response = []
        for i in range(0, inputLen):
            response.append(preProd[i] * posProd[i])
        
        return response
