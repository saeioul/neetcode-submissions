class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Capture frequency is a must. Need a map
        elementFreqMap = {}

        # Need a bucket list. The trick is the list needs to have as many buckets
        # as the original input list, because that would be the highest possible frequence.
        elementFreqBuckets = []
        for i in range(0, len(nums) + 1):
            elementFreqBuckets.append([])

        # Get the counts per element
        for anElement in nums:
            if anElement in elementFreqMap:
                elementFreqMap[anElement] += 1
            else:
                elementFreqMap[anElement] = 1

        # Since we already know key -> element and val -> frequency, we can map frequency
        # to our bucket.
        for key, value in elementFreqMap.items():
            elementFreqBuckets[value].append(key)

        # At this point we only need to traverse our bucket list and extract the keys:
        solutionArray = []
        for i in range(len(elementFreqBuckets) -1, 0, -1):
            bucketList = elementFreqBuckets[i]
            for foundElement in bucketList:
                solutionArray.append(foundElement)
                if k == len(solutionArray):
                    return solutionArray



        


        