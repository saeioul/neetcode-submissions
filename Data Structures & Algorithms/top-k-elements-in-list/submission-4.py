class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #Store the count of elements
        count = {}

        # In an array with length n, the topmost possible frequence is n
        # and  the lowet possible frequence is 0 for all the elements not in the array.
        # so we need to create n+1 sized array to hold the possible counts from 0 to n
        # This is our bucket for categorizing the frequency.
        # freq  = [[] for i in range(len(nums) + 1)] 
        freq = []
        for i in range(0, len(nums) + 1):
            freq.append([])

        # Count frequency. There are more fancy ways to do it but this is clear.
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # Because we already have our buckets lined up from 0 to n
        # we can just read the stored frequency and map it to a bucket
        # and add every key (the actual value to be ranked) into that bucket.
        for key, val in count.items():
            freq[val].append(key)

        solution = []
        # We look in reverse since that will yield the frequencies in descending order.
        for i in range(len(freq) -1, 0, -1):
            # Collect all the elements stored in that bucket.
            for num in freq[i]:
                solution.append(num)
                # Stop adding to the ranking when we have k elements
                if len(solution) == k:
                    return solution


        