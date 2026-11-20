class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Using buckets is the best option

        numCount = len(nums)

        freqBuckets = []
        valueCounts = {}
        responseArr = []

        # We need to account for all possible frequencies: 0 to numCount
        for i in range(0, numCount + 1):
            freqBuckets.append([])
        # Should look like:
        # [[], [], [], ... []]
        #  0 , 1 , 2 ,... numCount

        # We can now establish a mapping of seen values to their count:
        for aValue in nums:

            if aValue in valueCounts:
                valueCounts[aValue] += 1
            else:
                valueCounts[aValue] = 1

        # Then we can asign the values to their right buckets
        # Index bounds are guarded already: 0 is never going to happen
        # and the last bucket is always the highest possible count.
        for value, count in valueCounts.items():
            freqBuckets[count].append(value)

        # Finally, we collect only the K most frequent from the highest
        # frequency side. Starting in len(freqBuckets) should also work
        for j in range(numCount, -1, -1):
            for storedValue in freqBuckets[j]:
                if k == len(responseArr):
                    return responseArr
                
                responseArr.append(storedValue)
            
        return responseArr

