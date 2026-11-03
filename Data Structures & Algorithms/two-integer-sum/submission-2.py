class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Copy array, but also store index.
        localArray = []
        for i in range(0, len(nums)):
            localArray.append([nums[i], i])


        # Need to sort for the pointers technique to work
        localArray.sort()
        
        # Init pointers
        i = 0 # Left to rigth
        j = len(nums) -1 # Rigth to left

        while i < j :
            # localArray -> [ [value, idx], ...]
            # we are comparing the sum of the stored values.
            # which are located in the first element of the array inside the main array.
            if target == localArray[i][0] + localArray[j][0]:
                # Per requirement we need to return [smallerIdx, greaterIdx]
                # We are querying the second element of the array, where the index is.
                return [ min(localArray[i][1], localArray[j][1]),
                         max(localArray[i][1], localArray[j][1])]
            else:
                # In a sorted list of numbers, adding to the left index increases the sum,
                # and reducing right index lowers the sum
                if target > localArray[i][0] + localArray[j][0]:
                    i += 1
                else:
                    j -= 1
        
        return []
