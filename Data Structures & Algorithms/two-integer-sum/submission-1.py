class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap to store the values to index mappings
        diffHashMap = {}
        for i in range(0,len(nums)):
            currentVal = nums[i]
            diffHashMap[currentVal] = i
        print(f"Mapped values to indices: {diffHashMap}")

        # Find the value that satisfies: value = target - nums[i]
        for i in range(0, len(nums)):
            difference = target - nums[i]
            if difference in diffHashMap and diffHashMap[difference] != i:
                return [i, diffHashMap[difference]]
