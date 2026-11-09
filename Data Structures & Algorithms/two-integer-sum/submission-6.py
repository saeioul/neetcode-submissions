class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        The key for this problem is having the input sorted
        with their indices attached. In an ordered array, we can
        leverage the fact that the sum of the elements increase
        going left to right and decrease from right to left.
        '''

        sortedArray = []
        for i, n in enumerate(nums):
            sortedArray.append([n,i])

        sortedArray.sort()

        i = 0
        j = len(sortedArray) -1

        while i < j:
            if target == sortedArray[i][0] + sortedArray[j][0]:
                return [min(sortedArray[i][1], sortedArray[j][1]),
                        max(sortedArray[i][1], sortedArray[j][1])]
            # As long as we are below our target, we move left index
            if target > sortedArray[i][0] + sortedArray[j][0]:
                i += 1
            # If we exceeded target, we move right index
            else:
                j -=1
        
        return []



