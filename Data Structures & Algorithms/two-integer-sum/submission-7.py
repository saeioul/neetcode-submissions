class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Problem is easy once we have identified every value index:
        #  [[value, idx ] , [value, idx ] , ... [value, idx] }]

        sortedArray = []
        # We need to preserve the indices
        for i in range(0, len(nums)):
            value = nums[i] 
            sortedArray.append([value, i])

        # Cool thing about arrays in python is we can order in place
        sortedArray.sort()

        # Now we have the array sorted we can leverage the fact that
        # sums will increase wen picking values from legth to right
        # and decrease when picking values from right lo left.

        i = 0
        j = len(sortedArray) - 1

        while i < j:

            if sortedArray[i][0] + sortedArray[j][0] == target:
                return [min(sortedArray[i][1], sortedArray[j][1]),
                        max(sortedArray[i][1], sortedArray[j][1])]

            if sortedArray[i][0] + sortedArray[j][0] < target:
                i += 1
            else:
                j -= 1 

        
        return []


