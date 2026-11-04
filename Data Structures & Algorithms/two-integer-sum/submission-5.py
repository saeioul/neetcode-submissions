class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Copy input to avoid mutating external variable.
        # We also need to preserve their index mapping.
        sortedInputList = []
        for i in range(0, len(nums)):
            # Format is: [ [value, index] , ... ]
            sortedInputList.append([nums[i], i])

        # Leverage python sorting.
        sortedInputList.sort()

        print(f"Sorted input with indices: {sortedInputList}")

        #Initialize pointers:
        i = 0;
        j = len(sortedInputList) - 1

        #If value can be computed
        while i < j:
            leftValue  = sortedInputList[i][0]
            rightValue = sortedInputList[j][0]
            
            leftIndex  = sortedInputList[i][1]
            rightIndex = sortedInputList[j][1]

            if target == leftValue + rightValue:
                return([min(leftIndex, rightIndex), max(leftIndex, rightIndex)])
            else:
                if leftValue + rightValue < target:
                    i += 1 
                else:
                    j -= 1
        
        return []
        