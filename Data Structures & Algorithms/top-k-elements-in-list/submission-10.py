class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        '''
        The key is the bucket-sort concept. It means we create an
        array whose indices are directly mapped to the possible 
        frequencies to be ranked.
        '''
        
        # We need an extra element to hold from 0 to n
        # [ [], [], ..., []]
        #    0,  1, ..., n
        bucketList = []
        for i in range(0, len(nums) + 1):
            bucketList.append([])

        # Now we can count elements
        freqMap = {}

        for i in range(0, len(nums)):
            if nums[i] in freqMap:
                freqMap[nums[i]] += 1
            else:
                freqMap[nums[i]] = 1

        # Since we have a nice element to frequency map
        # we can do the bucket sort in a single pass
        for value, frequency in freqMap.items():
            bucketList[frequency].append(value)

        # With the bucket list built, we can extract the
        # requested k elements
        response = []
        for i in range(len(bucketList) -1 , 0, -1):
            for aValue in bucketList[i]:
                response.append(aValue)
                if k == len(response):
                    return response
                
        
    
            
