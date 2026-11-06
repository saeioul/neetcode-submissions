class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # The key for this problem is having a bucket-sort paired with a hashmap
        n = len(nums)
        freqBuckets = []
        freqMap     = {}
        solutionArr = []

        # We need as many buckets as the input list has plus one, since
        # that is the maximum possible frequency (even though frequency 0 will store nothing)
        #  values    [  ,[key1,key2...], ... , [keyN]]
        #  frequency   0, 1,             , .... , n + 1   
        for i in range(0, n + 1):
            freqBuckets.append([])


        # Let's count elements!
        for aNum in nums:
            if aNum in freqMap:
                freqMap[aNum] += 1
            else:
                freqMap[aNum] = 1
    
        # And now place the proper keys in their frequency bucket
        # frequency is guaranteed to stay in the array range since it cannot
        # be more thant the bucket list.
        for value, frequency in freqMap.items():
            freqBuckets[frequency].append(value)


        # Proceed to return the topK
        for i in range(len(freqBuckets) - 1, 0, -1):
            currentBucket = freqBuckets[i]
            for aValue in currentBucket:
                solutionArr.append(aValue)
                if len(solutionArr) == k:
                    return solutionArr
                



        


        